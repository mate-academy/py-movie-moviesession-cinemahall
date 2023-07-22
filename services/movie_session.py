from datetime import datetime
from typing import Optional

from db.models import MovieSession
from django.db.models import QuerySet


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movies_sessions(
        session_date: Optional[str] = None
) -> QuerySet:
    if session_date:
        return MovieSession.objects.filter(
            show_time__date=session_date
        )
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: Optional[str] = None,
        movie_id: Optional[int] = None,
        cinema_hall_id: Optional[int] = None
) -> QuerySet:
    sess = MovieSession.objects.get(id=session_id)

    if show_time:
        sess.show_time = show_time
    if movie_id:
        sess.movie_id = movie_id
    if cinema_hall_id:
        sess.cinema_hall_id = cinema_hall_id
    sess.save()
    return sess


def delete_movie_session_by_id(
        session_id: int
) -> MovieSession:
    MovieSession.objects.filter(
        id=session_id
    ).delete()
