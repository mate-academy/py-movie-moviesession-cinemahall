import datetime
from typing import Optional

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
    movie_show_time: datetime,
    movie_id: int,
    cinema_hall_id: int
) -> None:

    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movies_sessions(
    session_date: Optional[datetime.datetime] = None
) -> QuerySet:
    movie_session = MovieSession.objects.all()

    if session_date:
        movie_session = movie_session.filter(show_time__date=session_date)

    return movie_session


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
    session_id: int,
    show_time: Optional[datetime.datetime] = None,
    movie_id: Optional[int] = None,
    cinema_hall_id: Optional[int] = None
) -> None:
    movie_session = MovieSession.objects.filter(id=session_id)

    update_data = {}

    if show_time is not None:
        update_data["show_time"] = show_time
    if movie_id is not None:
        update_data["movie_id"] = movie_id
    if cinema_hall_id is not None:
        update_data["cinema_hall_id"] = cinema_hall_id

    movie_session.update(**update_data)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
