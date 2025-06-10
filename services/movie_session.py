from typing import Optional
from datetime import datetime

from django.db.models import QuerySet
from django.core.exceptions import ObjectDoesNotExist

from db.models import MovieSession


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


def get_movies_sessions(date: Optional[str] = None) -> QuerySet:
    sessions = MovieSession.objects.select_related("movie", "cinema_hall")
    if date:
        sessions = sessions.filter(show_time__date=date)
    return sessions


def get_movie_session_by_id(session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=session_id)


def update_movie_session(
    session_id: int,
    show_time: Optional[datetime] = None,
    movie_id: Optional[int] = None,
    cinema_hall_id: Optional[int] = None
) -> MovieSession:
    session = MovieSession.objects.get(id=session_id)
    if show_time:
        session.show_time = show_time
    if movie_id:
        session.movie_id = movie_id
    if cinema_hall_id:
        session.cinema_hall_id = cinema_hall_id
    session.save()
    return session


def delete_movie_session_by_id(session_id: int) -> None:
    try:
        session = MovieSession.objects.get(id=session_id)
        session.delete()
    except ObjectDoesNotExist:
        pass
