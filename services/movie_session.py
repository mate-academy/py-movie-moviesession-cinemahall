from django.db.models import QuerySet
from db.models import MovieSession
from datetime import datetime


def create_movie_session(
    movie_show_time: datetime,
    movie_id: int,
    cinema_hall_id: int
) -> MovieSession:
    new_movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )
    return new_movie_session


def get_movies_sessions(
    session_date: str = None
) -> QuerySet:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
    session_id: int,
    show_time: datetime = None,
    movie_id: int = None,
    cinema_hall_id: int = None
) -> None:
    dict_ms = {}
    update_ms = MovieSession.objects.filter(id=session_id)
    if show_time:
        dict_ms["show_time"] = show_time
    if movie_id:
        dict_ms["movie_id"] = movie_id
    if cinema_hall_id:
        dict_ms["cinema_hall_id"] = cinema_hall_id
    update_ms.update(**dict_ms)


def delete_movie_session_by_id(
    session_id: int
) -> None:
    MovieSession.objects.filter(id=session_id).delete()
