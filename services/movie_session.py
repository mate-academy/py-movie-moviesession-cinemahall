from datetime import datetime
from typing import Optional

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
    movie_show_time: str, movie_id: int, cinema_hall_id: int
) -> MovieSession:
    show_time = movie_show_time
    movie_session = MovieSession(
        show_time=show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )
    movie_session.save()
    return movie_session


def get_movies_sessions(
    session_date: Optional[str] = None
) -> QuerySet:
    if session_date:
        date = (
            datetime.strptime(session_date, "%Y-%m-%d").date()
        )
        movie_sessions = (
            MovieSession.objects.filter(show_time__date=date)
        )
    else:
        movie_sessions = MovieSession.objects.all()
    return movie_sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: Optional[str] = None,
        movie_id: Optional[int] = None,
        cinema_hall_id: Optional[int] = None) -> MovieSession:
    movie_session = MovieSession.objects.get(id=session_id)
    if show_time:
        if isinstance(show_time, str):
            show_time = datetime.fromisoformat(show_time)
        movie_session.show_time = show_time
    if movie_id:
        movie_session.movie_id = movie_id
    if cinema_hall_id:
        movie_session.cinema_hall_id = cinema_hall_id
    movie_session.save()
    return movie_session


def delete_movie_session_by_id(session_id: Optional[int]) -> None:
    movie_session = get_movie_session_by_id(session_id)
    movie_session.delete()
