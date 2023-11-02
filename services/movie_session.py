from __future__ import annotations

from datetime import datetime
from typing import List

from db.models import MovieSession, CinemaHall
from services.movie import get_movie_by_id


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=CinemaHall.objects.get(id=cinema_hall_id),
        movie=get_movie_by_id(movie_id)
    )


def get_movies_sessions(
        session_date: str = None
) -> List[MovieSession]:
    if session_date:
        year, month, day = session_date.split("-")
        return MovieSession.objects.filter(
            show_time__year=year,
            show_time__month=month,
            show_time__day=day
        ).all()
    return MovieSession.objects.all()


def get_movie_session_by_id(
        movie_session_id: int
) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> MovieSession:
    movie_session = get_movie_session_by_id(session_id)
    if show_time:
        movie_session.show_time = show_time
    if movie_id:
        movie_session.movie = get_movie_by_id(movie_id)
    if cinema_hall_id:
        movie_session.cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    movie_session.save()
    return movie_session


def delete_movie_session_by_id(
        session_id: int
) -> None:
    MovieSession.objects.get(id=session_id).delete()
