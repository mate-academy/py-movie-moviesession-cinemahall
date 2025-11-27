from datetime import datetime

from django.db.models import QuerySet

import init_django_orm  # noqa: F401

from db.models import MovieSession, CinemaHall, Movie


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> None:

    movie_session = MovieSession(
        show_time=movie_show_time,
        cinema_hall=cinema_hall_id,
        movie=movie_id
    )
    movie_session.save()


def get_movies_sessions(
        session_date: str = None
) -> QuerySet[MovieSession]:
    sessions = MovieSession.objects.all()
    if session_date:
        sessions = sessions.filter(show_time__date=session_date)
    return sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    sessions = MovieSession.objects.get(id=movie_session_id)
    return sessions


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    session = MovieSession.objects.get(id=session_id)
    if show_time:
        session.show_time = show_time

    if movie_id:
        session.movie = movie_id

    if cinema_hall_id:
        session.cinema_hall = cinema_hall_id

    session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    session = MovieSession.objects.get(id=session_id)
    session.delete()
