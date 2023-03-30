from typing import Optional

from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from db.models import MovieSession


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    new_movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )
    return new_movie_session


def get_movies_sessions(session_date: str = None) -> QuerySet[MovieSession]:
    movie_session = MovieSession.objects.all()
    if session_date is not None:
        return movie_session.filter(show_time__date=session_date)
    return movie_session


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    movie_session_by_id = get_object_or_404(MovieSession, id=movie_session_id)
    return movie_session_by_id


def update_movie_session(
        session_id: int,
        show_time: Optional[str] = None,
        movie_id: Optional[int] = None,
        cinema_hall_id: Optional[int] = None
) -> None:
    movie_session = get_movie_session_by_id(session_id)
    if show_time:
        movie_session.show_time = show_time
    if movie_id:
        movie_session.movie_id = movie_id
    if cinema_hall_id:
        movie_session.cinema_hall_id = cinema_hall_id
    movie_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    movie_session = get_movie_session_by_id(session_id)
    movie_session.delete()
