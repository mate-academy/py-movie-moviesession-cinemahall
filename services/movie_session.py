from typing import Optional

from django.db.models import QuerySet
from db.models import MovieSession
from db.models import Movie


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movies_sessions(
        session_date: str = None
) -> QuerySet:
    movie_sessions_in_this_date = MovieSession.objects.all()
    if session_date is not None:
        movie_sessions_in_this_date = movie_sessions_in_this_date.filter(
            show_time__date=session_date
        )
    return movie_sessions_in_this_date


def get_movie_session_by_id(
    movie_session_id: int
) -> Movie | None:
    return MovieSession.objects.get(pk=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: Optional[str] = None,
        movie_id: Optional[list[int]] = None,
        cinema_hall_id: Optional[list[int]] = None
) -> None:
    movie_sessions = get_movie_session_by_id(session_id)
    if show_time is not None:
        movie_sessions.show_time = show_time
    if movie_id is not None:
        movie_sessions.movie_id = movie_id
    if cinema_hall_id is not None:
        movie_sessions.cinema_hall_id = cinema_hall_id
    movie_sessions.save()


def delete_movie_session_by_id(session_id: int) -> None:
    get_movie_session_by_id(session_id).delete()
