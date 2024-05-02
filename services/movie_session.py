from django.db.models import QuerySet

from django.utils.dateparse import parse_date
from datetime import datetime

from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=cinema_hall_id,
        movie=movie_id
    )


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()


def update_movie_session(
    session_id: int,
    show_time: datetime = None,
    movie_id: int = None,
    cinema_hall_id: int = None
) -> MovieSession:
    movie_session = MovieSession.objects.get(id=session_id)

    if show_time:
        movie_session.show_time.set(show_time)
    if movie_id:
        movie_session.movie.set(movie_id)
    if cinema_hall_id:
        movie_session.cinema_hall.set(cinema_hall_id)

    return movie_session


def get_movies_sessions(
        session_date: str
) -> QuerySet[MovieSession] | MovieSession:
    date_obj = parse_date(session_date)
    session = MovieSession.objects.filter(date=date_obj)
    if session:
        return session
    return MovieSession.objects.all()
