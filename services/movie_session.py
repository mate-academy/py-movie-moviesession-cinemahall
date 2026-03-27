from typing import Optional

from db.models import MovieSession
from django.db.models import QuerySet
from django.shortcuts import get_object_or_404


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


def get_movies_sessions(session_date: Optional[str] = None) -> QuerySet:
    queryset = MovieSession.objects.all()

    if session_date is not None:
        queryset = queryset.filter(show_time__date=session_date)

    return queryset


def get_movie_session_by_id(
        movie_session_id: int
) -> MovieSession:
    return get_object_or_404(MovieSession, id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: Optional[str] = None,
        movie_id: Optional[int] = None,
        cinema_hall_id: Optional[int] = None
) -> None:
    update_session = get_object_or_404(MovieSession, id=session_id)

    if show_time is not None:
        update_session.show_time = show_time
    if cinema_hall_id is not None:
        update_session.cinema_hall_id = cinema_hall_id
    if movie_id is not None:
        update_session.movie_id = movie_id

    update_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    get_movie_session_by_id(session_id).delete()
