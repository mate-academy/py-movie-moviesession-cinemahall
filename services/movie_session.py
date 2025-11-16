# services/movie_session.py
from typing import Optional
from django.db import transaction
from django.db.models import QuerySet
from db.models import MovieSession, Movie, CinemaHall
import datetime


def create_movie_session(
        movie_show_time: datetime.datetime,
        movie_id: int, cinema_hall_id: int) -> MovieSession:
    movie = Movie.objects.get(id=movie_id)
    hall = CinemaHall.objects.get(id=cinema_hall_id)
    return MovieSession.objects.create(
        show_time=movie_show_time, movie=movie, cinema_hall=hall)


def get_movies_sessions(session_date: Optional[str] = None) -> QuerySet:
    qs = MovieSession.objects.all()
    if session_date:
        # конвертуємо рядок у дату
        year, month, day = [int(x) for x in session_date.split("-")]
        date_obj = datetime.date(year, month, day)
        qs = qs.filter(show_time__date=date_obj)
    return qs


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


@transaction.atomic
def update_movie_session(session_id: int,
                         show_time: Optional[datetime.datetime] = None,
                         movie_id: Optional[int] = None,
                         cinema_hall_id: Optional[int] = None) -> MovieSession:
    session = MovieSession.objects.select_for_update().get(id=session_id)
    if show_time is not None:
        session.show_time = show_time
    if movie_id is not None:
        session.movie = Movie.objects.get(id=movie_id)
    if cinema_hall_id is not None:
        session.cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    session.save()
    return session


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
