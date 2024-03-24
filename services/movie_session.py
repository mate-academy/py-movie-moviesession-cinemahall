from typing import Optional

from django.utils.dateparse import parse_date

from django.db.models.query import QuerySet

from db.models import MovieSession

from datetime import datetime


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int,
) -> MovieSession:
    movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )
    return movie_session


def get_movies_sessions(
        session_date: Optional[str] = None
) -> QuerySet:
    if session_date:
        date = parse_date(session_date)
        return MovieSession.objects.filter(show_time__date=date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: Optional[datetime] = None,
        movie_id: Optional[int] = None,
        cinema_hall_id: Optional[int] = None
) -> MovieSession:
    session = MovieSession.objects.get(id=session_id)

    if show_time:
        session.show_time = show_time
    if movie_id:
        session.movie_id = movie_id
    if cinema_hall_id:
        session.cinema_hall_id = cinema_hall_id
    session.save()
    return session


def delete_movie_session_by_id(session_id: int) -> None:
    session = MovieSession.objects.get(id=session_id)
    session.delete()
