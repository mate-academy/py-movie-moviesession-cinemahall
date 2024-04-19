from datetime import datetime
from typing import Optional

from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404

from db.models import MovieSession
from services.movie import get_movie_by_id
from services.cinema_hall import get_cinema_hall_by_id


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> None:
    MovieSession.objects.create(show_time=movie_show_time,
                                movie_id=movie_id,
                                cinema_hall_id=cinema_hall_id)


def get_movies_sessions(session_date: Optional[datetime] = None) -> QuerySet:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> None | MovieSession:
    return get_object_or_404(MovieSession, id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: Optional[datetime] = None,
                         movie_id: Optional[int] = None,
                         cinema_hall_id: Optional[int] = None) -> None:
    if show_time or movie_id or cinema_hall_id:
        session = get_movie_session_by_id(session_id)
        if show_time:
            session.show_time = show_time
        if movie_id:
            session.movie = get_movie_by_id(movie_id)
        if cinema_hall_id:
            session.cinema_hall = get_cinema_hall_by_id(cinema_hall_id)
        session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    get_object_or_404(MovieSession, pk=session_id).delete()
