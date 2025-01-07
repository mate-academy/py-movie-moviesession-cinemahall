from django.db.models import QuerySet
from db.models import MovieSession
from datetime import datetime


def create_movie_session(
        movie_show_time: datetime,
        cinema_hall_id: int,
        movie_id: int) -> MovieSession:

    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=cinema_hall_id,
        movie=movie_id,
    )


def get_movie_session(
        session_date: datetime | str = None) -> QuerySet | MovieSession:
    queryset = MovieSession.objects.all()
    if session_date:
        queryset = queryset.filter(show_time=session_date)
    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: datetime | str = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> MovieSession:
    updated_session = MovieSession.objects.filter(id=session_id)
    if show_time:
        updated_session = updated_session.update(show_time=show_time)
    if movie_id:
        updated_session = updated_session.update(movie=movie_id)
    if cinema_hall_id:
        updated_session = updated_session.update(cinema_hall=cinema_hall_id)
    return updated_session


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
