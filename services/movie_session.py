import warnings
from db.models import MovieSession, Movie, CinemaHall
from datetime import time
from django.db.models import QuerySet


def create_movie_session(movie_show_time: time,
                         cinema_hall_id: int,
                         movie_id: int,) -> MovieSession:

    session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )
    return session


def get_movies_sessions(session_date: str = None) -> QuerySet:
    queryset = MovieSession.objects.all()
    if session_date:
        queryset = queryset.filter(show_time__date=session_date)
    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    if movie_session_id:
        return MovieSession.objects.get(id=movie_session_id)
    else:
        return "No such Id"


def update_movie_session(session_id: int,
                         show_time: time = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> None:
    if session_id:
        session = MovieSession.objects.get(id=session_id)
    if show_time:
        session.show_time = show_time
    if movie_id:
        movie_instance = Movie.objects.get(id=movie_id)
        session.movie = movie_instance
    if cinema_hall_id:
        cinema_hall_instance = CinemaHall.objects.get(id=cinema_hall_id)
        session.cinema_hall = cinema_hall_instance
    session.save()


def delete_movie_session_by_id(session_id: int = None) -> MovieSession:
    session = MovieSession.objects.get(id=session_id)
    return session.delete()
