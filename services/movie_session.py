import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime.datetime,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        id=movie_id,
        cinema_hall=cinema_hall_id
    )

def get_movie_sessions(session_date: str) -> QuerySet:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    else:
        return MovieSession.objects.all()

def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    try:
        return MovieSession.objects.get(id=movie_session_id)
    except ObjectDoesNotExist:
        raise ValueError(f"MovieSession with id {movie_session_id} does not exist")


def update_movie_session(
        session_id: int,
        show_time: datetime.datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    update_date = {}
    if show_time:
        update_date["show_time"] = show_time
    if movie_id:
        update_date["movie_id"] = movie_id
    if cinema_hall_id:
        update_date["cinema_hall_id"] = cinema_hall_id
    if update_date:
        MovieSession.objects.filter(id=session_id).update(**update_date)

def delete_movie_session_by_id(session_id: int) -> None:
    try:
        session = MovieSession.objects.get(id=session_id)
        session.delete()
    except ObjectDoesNotExist:
        raise ValueError(f"MovieSession with id {session_id} does not exist")
