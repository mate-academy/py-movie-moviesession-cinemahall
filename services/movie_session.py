from typing import Optional
from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from db.models import MovieSession


def create_movie_session(movie_show_time: str,
                         movie_id: int,
                         cinema_hall_id: int) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(session_date: Optional[str] = None) -> QuerySet:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> QuerySet:
    session = MovieSession.objects.filter(id=movie_session_id)
    return get_object_or_404(session)


def update_movie_session(session_id: int,
                         show_time: Optional[str] = None,
                         movie_id: Optional[int] = None,
                         cinema_hall_id: Optional[int] = None) -> None:
    updated_ms = MovieSession.objects.get(id=session_id)
    if show_time:
        updated_ms.show_time = show_time
    if movie_id:
        updated_ms.movie_id = movie_id
    if cinema_hall_id:
        updated_ms.cinema_hall_id = cinema_hall_id
    updated_ms.save()


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
