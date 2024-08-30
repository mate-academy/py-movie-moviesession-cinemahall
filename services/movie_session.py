from django.core.exceptions import ObjectDoesNotExist
from db.models import MovieSession, CinemaHall, Movie
from datetime import date, datetime
from typing import Optional


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int,
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id,
    )


def get_movies_sessions(session_date: str = "") -> MovieSession | None:
    if session_date:
        year, month, day = session_date.split("-")
        return MovieSession.objects.filter(
            show_time__date=date(int(year), int(month), int(day)),
        )
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_id)


def update_movie_session(
        session_id: int,
        show_time: Optional[datetime] = None,
        movie_id: Optional[int] = None,
        cinema_hall_id: Optional[int] = None
) -> None:
    try:
        movie_session = MovieSession.objects.get(id=session_id)
    except ObjectDoesNotExist:
        print(f"Movie Session with ID {session_id} does not exist")
    else:
        if show_time:
            movie_session.show_time = show_time
        if cinema_hall_id:
            movie_session.cinema_hall = (
                CinemaHall.objects.get(id=cinema_hall_id)
            )
        if movie_id:
            movie_session.movie = Movie.objects.get(id=movie_id)
        movie_session.save()
        return movie_session
    return None


def delete_movie_session_by_id(session_id: int) -> None:
    movie_session = MovieSession.objects.get(id=session_id)
    movie_session.delete()
    return movie_session
