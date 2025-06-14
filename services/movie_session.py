from typing import Optional

from django.db.models import QuerySet
from django.utils.timezone import make_naive, get_current_timezone

import settings
from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    if settings.USE_TZ:
        movie_show_time = make_naive(movie_show_time, get_current_timezone())

    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=CinemaHall.objects.get(id=cinema_hall_id),
        movie=Movie.objects.get(id=movie_id)
    )


def get_movies_sessions(session_date: Optional[str] = None) -> QuerySet:
    query = MovieSession.objects.all()
    if session_date:
        query = query.filter(show_time__date=session_date)
    return query


def get_movie_session_by_id(movie_session_id: int) -> Optional[MovieSession]:
    return MovieSession.objects.filter(id=movie_session_id).first()


def update_movie_session(
        session_id: int,
        show_time: Optional[str] = None,
        movie_id: Optional[int] = None,
        cinema_hall_id: Optional[int] = None
) -> Optional[MovieSession]:
    session = MovieSession.objects.filter(id=session_id).first()
    if session:
        if show_time:
            session.show_time = show_time
        if movie_id:
            session.movie_id = movie_id
        if cinema_hall_id:
            session.cinema_hall_id = cinema_hall_id
        session.save()
    return session


def delete_movie_session_by_id(session_id: int) -> None:
    return MovieSession.objects.filter(id=session_id).delete()
