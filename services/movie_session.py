from __future__ import annotations

from datetime import datetime
from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
        movie_show_time: str | datetime,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(session_date: str | None = None) -> QuerySet:
    if session_date is not None:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: str | datetime | None = None,
        movie_id: int | None = None,
        cinema_hall_id: int | None = None,
) -> None:
    data = {key: value for key, value in [("show_time", show_time),
                                          ("movie_id", movie_id),
                                          ("cinema_hall_id", cinema_hall_id)]
            if value is not None}

    MovieSession.objects.filter(id=session_id).update(**data)


def delete_movie_session_by_id(session_id: int) -> None:
    get_movie_session_by_id(session_id).delete()
