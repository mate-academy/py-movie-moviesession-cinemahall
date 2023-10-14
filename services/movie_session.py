from typing import Any

from django.db.models import QuerySet

from db.models import MovieSession

from datetime import datetime, date


def create_movie_session(
        movie_show_time: Any,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    show_time = movie_show_time

    if type(movie_show_time) == str:
        show_time = datetime.strptime(movie_show_time, "%Y-%m-%d %H:%M:%S")

    movie_session = MovieSession.objects.create(
        show_time=show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )

    return movie_session


def get_movies_sessions(session_date: date = None) -> QuerySet:
    movie_sessions = MovieSession.objects.all()

    if session_date:
        movie_sessions = movie_sessions.filter(show_time__date=session_date)

    return movie_sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None) -> None:
    movie_session = get_movie_session_by_id(session_id)

    if show_time:
        movie_session.show_time = show_time
    if movie_id:
        movie_session.movie_id = movie_id
    if cinema_hall_id:
        movie_session.cinema_hall_id = cinema_hall_id

    movie_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
