from datetime import datetime

from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int,
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(session_date: str = None) -> QuerySet[MovieSession]:
    movie_sessions = MovieSession.objects.all()
    if session_date:
        movie_sessions = movie_sessions.filter(show_time__date=session_date)

    return movie_sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return get_object_or_404(MovieSession, pk=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = 0,
        cinema_hall_id: int = 0,
) -> None:
    update_fields = {}

    if show_time:
        update_fields["show_time"] = show_time

    if movie_id:
        update_fields["movie_id"] = movie_id

    if cinema_hall_id:
        update_fields["cinema_hall_id"] = cinema_hall_id

    if update_fields:
        MovieSession.objects.filter(id=session_id).update(**update_fields)


def delete_movie_session_by_id(movie_session_id: int) -> None:
    get_movie_session_by_id(movie_session_id).delete()
