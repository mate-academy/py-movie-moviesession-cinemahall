from typing import Optional

from django.db.models import QuerySet

import init_django_orm  # noqa: F401
from db.models import MovieSession
from django.shortcuts import get_object_or_404


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    new_session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )
    return new_session


def get_movies_sessions(session_date: Optional[str] = None) -> QuerySet[MovieSession]:
    queryset = MovieSession.objects.all()
    if session_date:
        queryset = queryset.filter(show_time__date=session_date)
    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return get_object_or_404(MovieSession, id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: Optional[str] = None,
                         movie_id: Optional[int] = None,
                         cinema_hall_id: Optional[int] = None
                         ) -> None:
    session = get_object_or_404(MovieSession, id=session_id)
    if show_time:
        session.show_time = show_time
    if movie_id:
        session.movie_id = movie_id
    if cinema_hall_id:
        session.cinema_hall_id = cinema_hall_id
    session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    get_object_or_404(MovieSession, id=session_id).delete()
