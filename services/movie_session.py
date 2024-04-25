from db.models import MovieSession, Movie, CinemaHall
from django.db.models.query import QuerySet
from datetime import datetime


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> None:
    movie = Movie.objects.get(id=movie_id)
    hall = CinemaHall.objects.get(id=cinema_hall_id)
    MovieSession.objects.create(show_time=movie_show_time,
                                cinema_hall=hall,
                                movie=movie)


def get_movies_sessions(session_date: str = None) -> QuerySet:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: str = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> None:
    session = MovieSession.objects.filter(id=session_id)

    if show_time:
        session.update(show_time=show_time)
    if movie_id:
        movie = Movie.objects.get(id=movie_id)
        session.update(movie=movie)
    if cinema_hall_id:
        hall = CinemaHall.objects.get(id=cinema_hall_id)
        session.update(cinema_hall=hall)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
