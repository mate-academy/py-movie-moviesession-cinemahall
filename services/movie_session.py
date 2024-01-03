from typing import Optional, Union
from datetime import datetime
from django.db.models.query import QuerySet

from db.models import MovieSession


def create_movie_session(
    movie_show_time: str, movie_id: int, cinema_hall_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time, movie_id=movie_id, cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(
    session_date: Optional[Union[str, datetime]] = None
) -> QuerySet[MovieSession]:
    if session_date:
        queryset = MovieSession.objects.all().filter(show_time__date=session_date)
        return queryset
    else:
        return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    movie = MovieSession.objects.all().get(pk=movie_session_id)
    return movie


def update_movie_session(
    session_id: int,
    show_time: Optional[str] = None,
    movie_id: Optional[int] = None,
    cinema_hall_id: Optional[int] = None,
) -> QuerySet[MovieSession]:
    queryset = MovieSession.objects.filter(pk=session_id)
    if cinema_hall_id is not None:
        queryset.update(cinema_hall_id=cinema_hall_id)
    if movie_id is not None:
        queryset.update(movie_id=movie_id)
    if show_time is not None:
        queryset.update(show_time=show_time)
    return queryset


def delete_movie_session_by_id(session_id: int) -> None:
    movie = MovieSession.objects.all().get(pk=session_id)
    movie.delete()
