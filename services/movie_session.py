from datetime import datetime
from typing import List

from db.models import MovieSession


def create_movie_session(
        movie_id: int,
        movie_show_time: datetime,
        cinema_hall_id: int
) -> MovieSession:
    new_movie_session = MovieSession.objects.create(
        show_time=movie_show_time
    )

    new_movie_session.movie_id = movie_id
    new_movie_session.movie_hall_id = cinema_hall_id

     return new_movie_session


def get_movies_sessions(session_date: datetime) -> List[MovieSession]:
    movie_sessions = MovieSession.objects.all()
    if session_date:
        movie_sessions = movie_sessions.filter(session_date)
        return movie_sessions
    else:
        return movie_sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    movie_session = MovieSession.objects.get(movie_id=movie_session_id)
    return movie_session


def update_movie_session(
        session_id: int,
        show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    movie_session = MovieSession.objects.get(session_id=session_id)
    if show_time:
        movie_session.show_time = show_time
    if movie_id:
        movie_session.movie_id = movie_id
    if cinema_hall_id:
        movie_session.movie_hall_id = cinema_hall_id

    return movie_session


def delete_movie_session_by_id(session_id: int) -> None:
    delete_movie_session = MovieSession.objects.get(session_id=session_id)
    delete_movie_session.delete()