from typing import Optional
from django.db.models import QuerySet
from db.models import MovieSession
import datetime


def create_movie_session(movie_id: int,
                         cinema_hall_id: int,
                         movie_show_time: datetime.datetime) -> MovieSession:
    return MovieSession.objects.create(
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id,
        show_time=movie_show_time
    )


def get_movies_sessions(session_date: Optional[str] = None) -> QuerySet:
    qs = MovieSession.objects.all()
    if session_date:
        year, month, day = [int(x) for x in session_date.split("-")]
        qs = qs.filter(show_time__date=datetime.date(year, month, day))
    return qs


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: Optional[datetime.datetime] = None,
                         movie_id: Optional[int] = None,
                         cinema_hall_id: Optional[int] = None) -> MovieSession:
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
    MovieSession.objects.filter(id=session_id).delete()
