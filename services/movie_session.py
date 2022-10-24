import datetime

from django.db.models.query import QuerySet
from db.models import MovieSession


def create_movie_session(movie_show_time: datetime.datetime,
                         cinema_hall_id: int, movie_id: int) -> None:
    MovieSession.objects.create(show_time=movie_show_time,
                                cinema_hall_id=cinema_hall_id,
                                movie_id=movie_id)


def get_movies_sessions(session_date: str = None) -> QuerySet:
    movies_sessions = MovieSession.objects.all()

    if session_date:
        movies_sessions = movies_sessions.filter(show_time__date=session_date)

    return movies_sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime.datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    movie_session = MovieSession.objects.filter(id=session_id)

    if show_time:
        movie_session.update(show_time=show_time)
    if movie_id:
        movie_session.update(movie_id=movie_id)
    if cinema_hall_id:
        movie_session.update(cinema_hall_id=cinema_hall_id)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
