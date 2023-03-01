from datetime import datetime
from db.models import MovieSession
from django.db.models import QuerySet
from typing import Optional


def create_movie_session(
    movie_show_time: datetime, movie_id: int, cinema_hall_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id,
    )


def get_movies_sessions(session_date: Optional[datetime] = None) -> QuerySet:
    query = MovieSession.objects.all()
    if session_date is not None:
        query = query.filter(show_time__date=session_date)
    return query


def get_movie_session_by_id(
        movie_session_id: Optional[int] = None
) -> QuerySet:
    query = MovieSession.objects.all()
    if movie_session_id is not None:
        query = MovieSession.objects.get(id=movie_session_id)
    return query


def update_movie_session(
    session_id: int,
    show_time: Optional[datetime] = None,
    movie_id: Optional[int] = None,
    cinema_hall_id: Optional[int] = None,
) -> None:
    query = {
        f"{key}": value for key, value in locals().items() if value is not None
    }
    query.pop("session_id")
    MovieSession.objects.filter(id=session_id).update(**query)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
