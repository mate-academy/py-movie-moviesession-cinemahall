import datetime
from typing import Optional

from django.db.models import QuerySet

from db.models import MovieSession, CinemaHall, Movie


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int,
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=CinemaHall.objects.get(id=cinema_hall_id),
        movie=Movie.objects.get(id=movie_id),
    )


def get_movies_sessions(session_date: datetime = None) -> QuerySet:
    query = MovieSession.objects.all()

    if session_date:
        query = query.filter(show_time__date=session_date)

    return query


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: Optional[int] = None,
        cinema_hall_id: Optional[int] = None,
) -> QuerySet:
    to_update = MovieSession.objects.filter(id=session_id)

    if show_time:
        to_update.update(show_time=show_time)

    if movie_id:
        to_update.update(movie=Movie.objects.get(id=movie_id))

    if cinema_hall_id:
        to_update.update(cinema_hall=CinemaHall.objects.get(id=cinema_hall_id))

    return to_update


def delete_movie_session_by_id(session_id: int) -> MovieSession:
    session_to_delete = MovieSession.objects.get(id=session_id)
    return session_to_delete.delete()
