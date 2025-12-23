from datetime import datetime
from typing import Optional

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movies_sessions(session_date: Optional[str] = None) -> QuerySet:
    movies_sessions_queryset = MovieSession.objects.all()
    if session_date:
        movies_sessions_queryset = movies_sessions_queryset.filter(
            show_time__date=session_date
        )
    return movies_sessions_queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(pk=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: Optional[datetime] = None,
                         movie_id: Optional[int] = None,
                         cinema_hall_id: Optional[int] = None) -> None:
    update_fields = {}
    if show_time:
        update_fields["show_time"] = show_time
    if movie_id:
        update_fields["movie"] = movie_id
    if cinema_hall_id:
        update_fields["cinema_hall"] = cinema_hall_id
    if update_fields:
        MovieSession.objects.filter(id=session_id).update(**update_fields)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
