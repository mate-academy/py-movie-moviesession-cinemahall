from datetime import datetime
from typing import Optional

from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    try:
        movie_session = MovieSession.objects.create(
            show_time=movie_show_time,
            movie_id=movie_id,
            cinema_hall_id=cinema_hall_id
        )
        return movie_session
    except Exception as e:
        return e


def get_movies_sessions(session_date: Optional[str] = None) -> QuerySet:
    movies_sessions = MovieSession.objects.all()
    if session_date:
        movies_sessions = movies_sessions.filter(show_time__date=session_date)
    return movies_sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return get_object_or_404(MovieSession, pk=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    try:
        movie_session = MovieSession.objects.get(pk=session_id)

        if show_time:
            movie_session.show_time = show_time
        if movie_id is not None:
            movie_session.movie_id = movie_id
        if cinema_hall_id is not None:
            movie_session.cinema_hall_id = cinema_hall_id

        movie_session.save()
    except MovieSession.DoesNotExist:
        pass


def delete_movie_session_by_id(session_id: int) -> None:
    movie_session = get_movie_session_by_id(session_id)
    if movie_session is not None:
        movie_session.delete()
