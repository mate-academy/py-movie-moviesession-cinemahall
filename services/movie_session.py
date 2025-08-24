from db.models import Movie as MovieModel, MovieSession, CinemaHall
from typing import Optional
import datetime
from django.db.models.query import QuerySet


def create_movie_session(
    movie_show_time,
    cinema_hall_id: int,
    movie_id: int,
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id,
    )


def get_movies_sessions(
    session_date: Optional[str] = None
) -> QuerySet[MovieSession]:
    qs = MovieSession.objects.all()
    if session_date:
        qs = qs.filter(show_time__date=session_date)
    return qs


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
    session_id: int,
    movie_show_time=None,
    cinema_hall_id: Optional[int] = None,
    movie_id: Optional[int] = None,
) -> Optional[MovieSession]:
    try:
        session = MovieSession.objects.get(id=session_id)
    except MovieSession.DoesNotExist:
        return None

    if movie_show_time is not None:
        session.show_time = movie_show_time
    if cinema_hall_id is not None:
        session.cinema_hall_id = cinema_hall_id
    if movie_id is not None:
        session.movie_id = movie_id

    session.save()
    return session


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
