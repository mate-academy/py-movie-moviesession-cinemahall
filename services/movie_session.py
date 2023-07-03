from db.models import MovieSession
from datetime import datetime

from django.db.models import QuerySet


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> MovieSession:
    return MovieSession(show_time=movie_show_time,
                        movie=movie_id,
                        cinema_hall=cinema_hall_id)


def get_movies_session(session_date: str = None) -> QuerySet:
    query = MovieSession.objects.all()
    if session_date:
        session_date = datetime.strptime(session_date, "%Y-%m-%d").date()
        query = query.filter(show_time=session_date)
    return query


def get_movie_session_by_id(movie_session_id: int) -> QuerySet:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_sessions(session_id: int,
                          show_time: datetime = None,
                          movie_id: int = None,
                          cinema_hall_id: int = None) -> None:
    session = MovieSession.objects.get(id=session_id)
    if show_time:
        session.update(show_time=show_time)
    if movie_id:
        session.update(movie=movie_id)
    if cinema_hall_id:
        session.update(cinema_hall=cinema_hall_id)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
