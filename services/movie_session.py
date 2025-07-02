from datetime import datetime
from db.models import MovieSession, Movie, CinemaHall
from django.db.models import QuerySet
from typing import Optional


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int) -> None:
    movie = Movie.objects.get(pk=movie_id)
    cinema_hall = CinemaHall.objects.get(pk=cinema_hall_id)
    MovieSession.objects.create(show_time=movie_show_time,
                                movie=movie,
                                cinema_hall=cinema_hall)


def get_movies_sessions(
        session_date: Optional[str] = None
) -> QuerySet[MovieSession]:
    if session_date is not None:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(pk=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: Optional[datetime] = None,
                         movie_id: Optional[int] = None,
                         cinema_hall_id: Optional[int] = None) -> None:
    session = get_movie_session_by_id(session_id)
    if show_time is not None:
        session.show_time = show_time
    if movie_id is not None:
        movie = Movie.objects.get(pk=movie_id)
        session.movie = movie
    if cinema_hall_id is not None:
        cinema_hall = CinemaHall.objects.get(pk=cinema_hall_id)
        session.cinema_hall = cinema_hall
    session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(pk=session_id).delete()
