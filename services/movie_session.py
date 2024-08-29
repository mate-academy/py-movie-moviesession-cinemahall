from __future__ import annotations
from datetime import datetime
from typing import Optional

from db.models import MovieSession
from django.db.models import QuerySet


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(session_date: Optional[str] = None) -> QuerySet:
    sessions = MovieSession.objects.all()

    if session_date:
        sessions = sessions.filter(show_time__date=session_date)

    return sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(pk=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: Optional[datetime] = None,
        movie_id: Optional[int] = None,
        cinema_hall_id: Optional[int] = None
) -> MovieSession | None:
    if not show_time and not movie_id and not cinema_hall_id:
        return None

    updated_movie_session = MovieSession.objects.get(pk=session_id)

    if show_time:
        updated_movie_session.show_time = show_time

    if movie_id:
        updated_movie_session.movie_id = movie_id

    if cinema_hall_id:
        updated_movie_session.cinema_hall_id = cinema_hall_id

    updated_movie_session.save()

    return updated_movie_session


def delete_movie_session_by_id(session_id: int) -> int:
    deleted_count, _ = get_movie_session_by_id(session_id).delete()
    return deleted_count
