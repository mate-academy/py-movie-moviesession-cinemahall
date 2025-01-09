from datetime import datetime
from typing import Optional

from django.db.models import QuerySet

from db.models import MovieSession


def get_movies_sessions(session_date: Optional[str] = None) -> QuerySet:
    if session_date is None:
        return MovieSession.objects.all()
    session_date = datetime.strptime(session_date, "%Y-%m-%d")
    return MovieSession.objects.filter(show_time__date=session_date)


def create_movie_session(movie_show_time: datetime, movie_id: int,
                         cinema_hall_id: int) -> None:
    MovieSession.objects.create(show_time=movie_show_time,
                                movie_id=movie_id,
                                cinema_hall_id=cinema_hall_id)


def get_movie_session_by_id(movie_session_id: int) -> MovieSession | None:
    try:
        return MovieSession.objects.get(id=movie_session_id)
    except MovieSession.DoesNotExist:
        return None


def update_movie_session(session_id: int, show_time: Optional[datetime] = None,
                         movie_id: Optional[int] = None,
                         cinema_hall_id: Optional[int] = None) -> None:
    session = get_movie_session_by_id(session_id)

    if show_time:
        session.show_time = show_time
    if movie_id:
        session.movie_id = movie_id
    if cinema_hall_id:
        session.cinema_hall_id = cinema_hall_id

    session.save()


def delete_movie_session_by_id(movie_session_id: int) -> None:
    session = MovieSession.objects.get(id=movie_session_id)
    session.delete()
