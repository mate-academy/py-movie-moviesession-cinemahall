import datetime

from django.db.models import QuerySet

from db import models
from db.models import CinemaHall, Movie, MovieSession


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    models.MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=CinemaHall.objects.get(id=cinema_hall_id),
        movie=Movie.objects.get(id=movie_id)
    )


def get_movies_sessions(session_date: str = None) -> QuerySet:
    if session_date:
        date_ = datetime.datetime.strptime(session_date, "%Y-%m-%d")
        return (models.MovieSession.objects.filter(show_time__date=date_))
    return models.MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return models.MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    if show_time:
        models.MovieSession.objects.filter(id=session_id).update(
            show_time=show_time
        )
    if movie_id:
        models.MovieSession.objects.filter(id=session_id).update(
            movie=movie_id
        )
    if cinema_hall_id:
        models.MovieSession.objects.filter(id=session_id).update(
            cinema_hall=cinema_hall_id
        )


def delete_movie_session_by_id(session_id: int) -> None:
    models.MovieSession.objects.filter(id=session_id).delete()
