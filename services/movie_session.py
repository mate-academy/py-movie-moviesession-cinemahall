from django.db.models import QuerySet
from db.models import MovieSession
from datetime import datetime


def create_movie_session(movie_show_time: datetime, movie_id: int,
                         cinema_hall_id: int) -> MovieSession:
    new_movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id,

    )
    return new_movie_session


def get_movies_sessions(session_date: str = None) -> QuerySet:
    qs = MovieSession.objects.all()
    if session_date:
        return qs.filter(show_time__date=session_date)
    return qs


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int, show_time: datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> MovieSession:
    new_session = MovieSession.objects.get(id=session_id)
    if show_time:
        new_session.show_time = show_time
    if movie_id:
        new_session.movie_id = movie_id
    if cinema_hall_id:
        new_session.cinema_hall_id = cinema_hall_id
    new_session.save()
    return new_session


def delete_movie_session_by_id(session_id: int) -> None:
    movie_to_be_deleted = MovieSession.objects.get(id=session_id)
    movie_to_be_deleted.delete()
