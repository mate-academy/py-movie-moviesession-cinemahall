from django.db import transaction
from django.db.models import QuerySet
from django.core.exceptions import ValidationError
from datetime import datetime
from typing import Optional
from db.models import MovieSession, CinemaHall


def create_movie_session(
    movie_show_time: datetime,
    movie_id: int,
    cinema_hall_id: int
) -> MovieSession:
    try:
        cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    except CinemaHall.DoesNotExist:
        raise CinemaHall.DoesNotExist(
            f"Cinema hall with ID {cinema_hall_id} does not exist"
        )

    overlapping_sessions = MovieSession.objects.filter(
        cinema_hall=cinema_hall,
        show_time__date=movie_show_time.date()
    ).filter(show_time__hour=movie_show_time.hour)

    if overlapping_sessions.exists():
        raise ValidationError(
            "Cinema hall is already booked for this time slot"
        )

    with transaction.atomic():
        movie_session = MovieSession.objects.create(
            show_time=movie_show_time,
            movie_id=movie_id,
            cinema_hall=cinema_hall
        )

    return movie_session


def get_movies_sessions(
    session_date: Optional[str] = None
) -> QuerySet[MovieSession]:
    sessions = MovieSession.objects.all().select_related(
        "movie", "cinema_hall"
    )

    if session_date:
        try:
            target_date = datetime.strptime(
                session_date, "%Y-%m-%d"
            ).date()
            sessions = sessions.filter(show_time__date=target_date)

        except ValueError:
            raise ValidationError(
                "Invalid date format. Use 'year-month-day' format "
                "(e.g., '2024-01-15')"
            )

    return sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    try:
        return MovieSession.objects.select_related(
            "movie", "cinema_hall"
        ).get(id=movie_session_id)
    except MovieSession.DoesNotExist:
        raise MovieSession.DoesNotExist(
            f"Movie session with ID {movie_session_id} does not exist"
        )


def update_movie_session(
    session_id: int,
    show_time: Optional[datetime] = None,
    movie_id: Optional[int] = None,
    cinema_hall_id: Optional[int] = None
) -> MovieSession:
    try:
        movie_session = MovieSession.objects.get(id=session_id)
    except MovieSession.DoesNotExist:
        raise MovieSession.DoesNotExist(
            f"Movie session with ID {session_id} does not exist"
        )

    with transaction.atomic():
        if show_time is not None:
            movie_session.show_time = show_time

        if movie_id is not None:
            movie_session.movie_id = movie_id

        if cinema_hall_id is not None:
            try:
                cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)

                if (cinema_hall != movie_session.cinema_hall
                        or (show_time
                            and show_time != movie_session.show_time)):

                    check_time = (
                        show_time if show_time else movie_session.show_time
                    )

                    overlapping_sessions = MovieSession.objects.filter(
                        cinema_hall=cinema_hall,
                        show_time__date=check_time.date()
                    ).filter(
                        show_time__hour=check_time.hour
                    ).exclude(id=session_id)

                    if overlapping_sessions.exists():
                        raise ValidationError(
                            "Cinema hall is already booked for this time slot"
                        )

                movie_session.cinema_hall = cinema_hall

            except CinemaHall.DoesNotExist:
                raise CinemaHall.DoesNotExist(
                    f"Cinema hall with ID {cinema_hall_id} does not exist"
                )

        movie_session.save()

    movie_session.refresh_from_db()
    return movie_session


def delete_movie_session_by_id(session_id: int) -> bool:
    try:
        movie_session = MovieSession.objects.get(id=session_id)

        movie_session.delete()
        return True

    except MovieSession.DoesNotExist:
        raise MovieSession.DoesNotExist(
            f"Movie session with ID {session_id} does not exist"
        )
