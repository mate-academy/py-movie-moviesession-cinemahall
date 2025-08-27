from typing import Optional
import datetime

from db.models import MovieSession
from django.db.models import QuerySet


def get_movies_sessions(date: Optional[str] = None) -> QuerySet[MovieSession]:
    """Zwraca wszystkie sesje filmowe lub filtrowane po dacie."""
    sessions = MovieSession.objects.all()
    if date:
        sessions = sessions.filter(show_time__date=date)
    return sessions


def create_movie_session(
    movie_show_time: datetime.datetime,
    cinema_hall_id: int,
    movie_id: int
) -> MovieSession:
    """Tworzy nową sesję filmową."""
    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id,
    )


def get_movie_session_by_id(session_id: int) -> MovieSession:
    """Zwraca sesję filmową po ID."""
    return MovieSession.objects.get(pk=session_id)


def update_movie_session(
    session_id: int,
    show_time: Optional[datetime.datetime] = None,
    cinema_hall_id: Optional[int] = None,
    movie_id: Optional[int] = None
) -> MovieSession:
    """Aktualizuje sesję filmową."""
    session = MovieSession.objects.get(pk=session_id)
    if show_time:
        session.show_time = show_time
    if cinema_hall_id:
        session.cinema_hall_id = cinema_hall_id
    if movie_id:
        session.movie_id = movie_id
    session.save()
    return session


def delete_movie_session_by_id(session_id: int) -> None:
    """Usuwa sesję filmową po ID."""
    MovieSession.objects.filter(pk=session_id).delete()
