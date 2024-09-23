from typing import Optional
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.db.models import QuerySet
from db.models import MovieSession, Movie, CinemaHall
from datetime import datetime


def create_movie_session(
    movie_show_time: datetime,
    movie_id: int,
    cinema_hall_id: int
) -> None:
    if not isinstance(movie_show_time, datetime):
        raise ValueError(
            "Invalid show time format. "
            "Please provide a valid datetime object."
        )
    try:
        movie = Movie.objects.get(id=movie_id)

    except Movie.DoesNotExist:
        raise ValueError(
            f"Cinema hall with ID {cinema_hall_id} does not exist.")

    try:
        cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)

    except CinemaHall.DoesNotExist:
        raise ValueError(f"Movie with ID {movie_id} does not exist.")

    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=cinema_hall,
        movie=movie
    )


def get_movies_sessions(
    session_date: Optional[str] = None
) -> QuerySet[MovieSession]:
    queryset = MovieSession.objects.all()
    if session_date:
        try:
            date_obj = datetime.strptime(session_date, "%Y-%m-%d")
            queryset = queryset.filter(show_time__date=date_obj.date())
        except ValueError:
            raise ValidationError(
                "Incorrect date format. Please use 'YYYY-MM-DD'."
            )
    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    try:
        return MovieSession.objects.get(id=movie_session_id)

    except ObjectDoesNotExist:
        raise ValidationError(
            f"Movie session with id {movie_session_id} does not exist."
        )


def update_movie_session(
    session_id: int,
    show_time: Optional[datetime] = None,
    movie_id: Optional[int] = None,
    cinema_hall_id: Optional[int] = None
) -> None:
    try:
        movie_session = MovieSession.objects.get(id=session_id)
    except MovieSession.DoesNotExist:
        raise ValueError(
            f"Movie session with the provided ID {session_id} does not exist."
        )

    if show_time:
        if isinstance(show_time, datetime):
            movie_session.show_time = show_time
        else:
            raise ValueError(
                f"Invalid show time format. Please provide a valid datetime."
            )

    if movie_id:
        try:
            movie_session.movie = Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            raise ValueError(
                f"Movie with the provided ID {movie_id} does not exist."
            )

    if cinema_hall_id:
        try:
            movie_session.cinema_hall = CinemaHall.objects.get(
                id=cinema_hall_id
            )
        except CinemaHall.DoesNotExist:
            raise ValueError(
                f"Cinema hall with the provided ID "
                f"{cinema_hall_id} does not exist."
            )

    movie_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    try:
        MovieSession.objects.get(id=session_id).delete()
    except MovieSession.DoesNotExist:
        raise ValueError(
            f"Movie session with ID {session_id} does not exist."
        )
