from datetime import datetime
from db.models import MovieSession
from db.models import CinemaHall
from services.movie import get_movie_by_id


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int):
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    new_session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=cinema_hall,
        movie=get_movie_by_id(movie_id=movie_id)
    )
    return new_session


def get_movies_sessions(session_date: datetime = None):
    movies_sessions = MovieSession.objects.all()
    if session_date:
        movies_sessions = movies_sessions.filter(
            show_time__date=session_date)
    return movies_sessions


def get_movie_session_by_id(movie_session_id: int):
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: int = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None):
    movie_session = MovieSession.objects.filter(id=session_id)
    if show_time:
        movie_session.update(show_time=show_time)

    if movie_id:
        movie_session.update(movie_id=movie_id)

    if cinema_hall_id:
        movie_session.update(cinema_hall_id=cinema_hall_id)


def delete_movie_session_by_id(session_id: int):
    session = MovieSession.objects.get(id=session_id)
    session.delete()
