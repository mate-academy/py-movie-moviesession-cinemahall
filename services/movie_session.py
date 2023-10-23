from datetime import datetime

from django.db.models import QuerySet
from django.utils import timezone

from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(movie_show_time: str,
                         movie_id: int,
                         cinema_hall_id: int) -> None:
    movie = Movie.objects.get(pk=movie_id)
    movie_show_time = timezone.make_aware(movie_show_time)
    cinema_hall = CinemaHall.objects.get(pk=cinema_hall_id)
    MovieSession.objects.create(
        show_time=movie_show_time,
        movie=movie,
        cinema_hall=cinema_hall
    )


def get_movies_sessions(session_date: str = None) -> QuerySet:
    movie_sessions = MovieSession.objects.all()
    if session_date:
        date = datetime.strptime(session_date, "%Y-%m-%d").date()
        movie_sessions = movie_sessions.filter(show_time__date=date)
    return movie_sessions


def get_movie_session_by_id(movie_session_id: int) -> QuerySet:
    return MovieSession.objects.filter(pk=movie_session_id).get()


def update_movie_session(session_id: int,
                         show_time: str = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> None:
    movie = Movie.objects.get(pk=movie_id)
    movie_show_time = timezone.make_aware(show_time)
    cinema_hall = CinemaHall.objects.get(pk=cinema_hall_id)
    MovieSession.objects.filter(pk=session_id).update(
        id=session_id,
        show_time=movie_show_time,
        cinema_hall=cinema_hall,
        movie=movie
    )


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(pk=session_id).delete()
