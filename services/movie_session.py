from django.db.models import QuerySet
from datetime import datetime
from db import models

from db.models import MovieSession
from services.movie import get_movie_by_id


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    movie = get_movie_by_id(movie_id)
    cinema_hall = models.CinemaHall.objects.get(id=cinema_hall_id)
    MovieSession.objects.create(show_time=movie_show_time,
                                movie=movie,
                                cinema_hall=cinema_hall)


def get_movies_sessions(session_date: str = None) -> QuerySet[MovieSession]:
    if session_date:
        session_date = datetime.strptime(session_date, "%Y-%m-%d")
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    session = get_movie_session_by_id(session_id)
    if show_time:
        session.show_time = show_time
    if movie_id:
        session.movie_id = models.Movie.objects.get(id=movie_id)
    if cinema_hall_id:
        session.cinema_hall_id = (models.CinemaHall.objects.get
                                  (id=cinema_hall_id))
    session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    get_movie_session_by_id(session_id).delete()
