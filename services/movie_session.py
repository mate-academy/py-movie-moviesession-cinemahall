from typing import Optional

from django.db.models import QuerySet

from db.models import MovieSession
import datetime as dt


def create_movie_session(
        movie_show_time: dt.datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )
    return movie_session


def get_movies_sessions(
        session_date: Optional[dt.datetime] = None
) -> QuerySet:
    movie_session = MovieSession.objects.all()
    if session_date:
        movie_session = movie_session.filter(
            show_time__date=session_date
        )
    return movie_session


def get_movie_session_by_id(session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=session_id)


def update_movie_session(
        session_id: int,
        show_time: Optional[dt.datetime] = None,
        movie_id: Optional[int] = None,
        cinema_hall_id: Optional[int] = None,
) -> MovieSession:
    if not any([cinema_hall_id, show_time, movie_id]):
        raise ValueError(
            "You won't be able to update without"
            " providing at least one argument"
        )

    session = MovieSession.objects.get(id=session_id)

    if cinema_hall_id is not None:
        session.cinema_hall_id = cinema_hall_id
    if movie_id is not None:
        session.movie_id = movie_id
    if show_time is not None:
        session.show_time = show_time

    session.save(update_fields=[
        "cinema_hall_id",
        "movie_id",
        "show_time"
    ])

    return session


def delete_movie_session_by_id(
        session_id: int
) -> None:
    return get_movie_session_by_id(
        session_id
    ).delete()
