from django.db.models import QuerySet
from typing import Optional

from db.models import MovieSession


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id)


def get_movies_sessions(session_date: Optional[str] = None) -> QuerySet:
    movie_sessions = MovieSession.objects.all()
    if session_date:
        movie_sessions = movie_sessions.filter(show_time__date=session_date)
    return movie_sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: Optional[str] = None,
                         movie_id: Optional[int] = None,
                         cinema_hall_id: Optional[int] = None) -> MovieSession:
    needed_session = MovieSession.objects.get(id=session_id)
    if show_time:
        needed_session.show_time = show_time
    needed_session.save()

    if movie_id is not None:
        needed_session = MovieSession.objects.filter(
            id=session_id
        ).update(
            movie=movie_id
        )

    if cinema_hall_id is not None:
        needed_session = MovieSession.objects.filter(
            id=session_id
        ).update(
            cinema_hall=cinema_hall_id
        )

    return needed_session


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
