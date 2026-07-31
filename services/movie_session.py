from datetime import datetime

from django.db.models import QuerySet

from typing import Optional

from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int,
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movies_sessions(
        session_date: str = None
) -> QuerySet:
    new_movie_session = MovieSession.objects.all()

    if session_date:
        new_movie_session = (
            new_movie_session.filter(show_time__date=session_date)
        )

    return new_movie_session


def get_movie_session_by_id(pk: int) -> MovieSession:
    return MovieSession.objects.get(id=pk)


def update_movie_session(
        session_id: int,
        show_time: Optional[datetime] = None,
        movie_id: Optional[int] = None,
        cinema_hall_id: Optional[int] = None,
) -> MovieSession:
    session = MovieSession.objects.get(pk=session_id)

    if show_time is not None:
        session.show_time = show_time
    if movie_id is not None:
        session.movie_id = movie_id
    if cinema_hall_id is not None:
        session.cinema_hall_id = cinema_hall_id

    session.save()
    return session


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
