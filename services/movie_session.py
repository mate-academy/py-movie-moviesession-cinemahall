from db.models import MovieSession
from typing import Any
from django.db.models.query import QuerySet


def create_movie_session(
        movie_show_time: Any,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(session_date: Any = None) -> QuerySet[MovieSession]:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: Any = None,
        movie_id: Any = None,
        cinema_hall_id: Any = None
) -> MovieSession:
    session = MovieSession.objects.get(id=session_id)

    if show_time is not None:
        session.show_time = show_time
    if movie_id is not None:
        session.movie_id = movie_id
    if cinema_hall_id is not None:
        session.cinema_hall_id = cinema_hall_id

    session.save()
    return session


def delete_movie_session_by_id(session_id: int) -> None:
    session = MovieSession.objects.get(id=session_id)
    session.delete()
