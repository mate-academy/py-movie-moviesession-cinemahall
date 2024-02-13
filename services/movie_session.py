from datetime import datetime

from django.db.models import QuerySet

import init_django_orm  # noqa: F401
from db.models import MovieSession, CinemaHall, Movie


def create_movie_session(
    movie_show_time: str,
    movie_id: int,
    cinema_hall_id: int,
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=CinemaHall.objects.get(id=cinema_hall_id),
        movie=Movie.objects.get(id=movie_id)
    )


def get_movies_sessions(
        session_date: str = None,
) -> QuerySet:
    if session_date:
        date = datetime.strptime(session_date, "%Y-%m-%d")
        return MovieSession.objects.filter(show_time__date=date)
    return MovieSession.objects.all()


def get_movie_session_by_id(
        movie_session_id: int
) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    session_to_update = MovieSession.objects.filter(id=session_id)

    if show_time:
        session_to_update.update(show_time=show_time)

    if movie_id:
        session_to_update.update(movie=movie_id)

    if cinema_hall_id:
        session_to_update.update(cinema_hall=cinema_hall_id)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
