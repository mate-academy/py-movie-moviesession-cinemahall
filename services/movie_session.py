from datetime import datetime

from django.db.models import QuerySet

import init_django_orm  # noqa: F401
from db.models import Movie
from db.models import MovieSession, CinemaHall


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    movie_session = MovieSession(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )
    movie_session.save()


def get_movies_sessions(session_date: str | None = None) -> QuerySet:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> QuerySet:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime | None = None,
        movie_id: int | None = None,
        cinema_hall_id: int | None = None
) -> None:
    session = MovieSession.objects.get(id=session_id)
    if show_time:
        session.show_time = show_time
    if movie_id:
        movie = Movie.objects.get(id=movie_id)
        session.movie = movie
    if cinema_hall_id:
        cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
        session.cinema_hall = cinema_hall
    session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
