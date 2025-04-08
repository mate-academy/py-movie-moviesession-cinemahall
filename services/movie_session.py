from __future__ import annotations

from django.db.models import QuerySet

from db.models import MovieSession

import datetime


def create_movie_session(
        movie_show_time: datetime.datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movies_sessions(session_date: str = None) -> QuerySet[MovieSession]:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: datetime.datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None
                         ) -> None:
    obj = MovieSession.objects.get(id=session_id)
    if show_time:
        obj.show_time = show_time
    if movie_id:
        obj.movie_id = movie_id
    if cinema_hall_id:
        obj.cinema_hall_id = cinema_hall_id
    obj.save()


def delete_movie_session_by_id(session_id: int) -> None:
    obj = MovieSession.objects.get(id=session_id)
    obj.delete()
