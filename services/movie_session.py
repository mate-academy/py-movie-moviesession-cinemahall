from datetime import datetime
from typing import Optional

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movies_sessions(session_date: Optional[str] = None) -> QuerySet:
    sessions = MovieSession.objects.all()

    if session_date:
        sessions = MovieSession.objects.filter(show_time__date=session_date)

    return sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(pk=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: Optional[datetime] = None,
        movie_id: Optional[int] = None,
        cinema_hall_id: Optional[int] = None
) -> None:
    if show_time or movie_id or cinema_hall_id:
        movie_session = MovieSession.objects.filter(pk=session_id)

        if show_time:
            movie_session.update(show_time=show_time)
        if movie_id:
            movie_session.update(movie_id=movie_id)
        if cinema_hall_id:
            movie_session.update(cinema_hall_id=cinema_hall_id)


def delete_movie_session_by_id(session_id: int) -> None:
    get_movie_session_by_id(session_id).delete()
