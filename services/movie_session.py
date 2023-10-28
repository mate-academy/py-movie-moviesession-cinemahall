from datetime import datetime
from typing import Optional

from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from db.models import MovieSession


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(session_date: str = None) -> QuerySet:
    sessions_qs = MovieSession.objects.all()
    if session_date is not None:
        sessions_qs = sessions_qs.filter(show_time__date=session_date)
    return sessions_qs


def get_movie_session_by_id(movie_session_id: int) -> Optional[MovieSession]:
    return get_object_or_404(MovieSession, id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None) -> None:
    movie_session = get_movie_session_by_id(session_id)
    if show_time is not None:
        movie_session.show_time = show_time
    if movie_id is not None:
        movie_session.movie_id = movie_id
    if cinema_hall_id is not None:
        movie_session.cinema_hall_id = cinema_hall_id
    movie_session.save()


def delete_movie_session_by_id(
        session_id: int
) -> None:
    movie_session = get_movie_session_by_id(session_id)
    movie_session.delete()
