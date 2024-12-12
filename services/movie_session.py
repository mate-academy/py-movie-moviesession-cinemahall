from datetime import datetime
from typing import Any

from django.db.models import QuerySet

from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(movie_show_time: Any,
                         movie_id: int,
                         cinema_hall_id: int) -> None:
    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    MovieSession.objects.get_or_create(show_time=movie_show_time,
                                       movie=movie,
                                       cinema_hall=cinema_hall)


def get_movies_sessions(session_date: str = None) -> QuerySet:
    if session_date:
        filtered_sessions = (MovieSession.objects.
                             filter(show_time__date=session_date))
        return filtered_sessions.all()
    else:
        return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> None:
    movie_session = MovieSession.objects.get(id=session_id)
    if show_time:
        movie_session.show_time = show_time
    if movie_id:
        movie = Movie.objects.get(id=movie_id)
        movie_session.movie = movie
    if cinema_hall_id:
        cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
        movie_session.cinema_hall = cinema_hall
    movie_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    movie_session = MovieSession.objects.get(id=session_id)
    movie_session.delete()
