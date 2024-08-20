from db.models import MovieSession, Movie, CinemaHall
from django.db.models import QuerySet
from datetime import datetime


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int) -> MovieSession:
    new_session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=CinemaHall.objects.get(id=cinema_hall_id),
        movie=Movie.objects.get(id=movie_id)
    )
    return new_session


def get_movies_sessions(session_date: datetime = None) -> QuerySet | MovieSession:
    movies_sessions = MovieSession.objects.all()
    if session_date:
        movies_sessions = MovieSession.objects.filter(show_time=session_date)
    return movies_sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(movie__id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None) -> None:
    MovieSession.objects.filter(id=session_id).update(
        show_time=show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
