from db.models import MovieSession
from django.db.models import QuerySet
import datetime


def create_movie_session(movie_show_time: datetime.datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> MovieSession:
    new_session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )
    return new_session


def get_movies_sessions(session_date: datetime.date = None) -> QuerySet:
    movies_sessions = MovieSession.objects.all()

    if session_date:
        movies_sessions = movies_sessions.filter(show_time__date=session_date)

    return movies_sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: datetime.datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> None:
    update_fields = {}

    if show_time:
        update_fields.update({"show_time": show_time})

    if movie_id:
        update_fields.update({"movie_id": movie_id})

    if cinema_hall_id:
        update_fields.update({"cinema_hall_id": cinema_hall_id})

    if update_fields:
        MovieSession.objects.filter(id=session_id).update(**update_fields)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
