import datetime
from typing import Optional

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime.datetime,
        movie_id: int,
        cinema_hall_id: int,
) -> MovieSession:
    MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id,
    )


def get_movies_sessions(session_date: Optional[str] = None) -> QuerySet:
    if session_date:
        date = datetime.datetime.strptime(session_date, "%Y-%m-%d").date()
        return MovieSession.objects.filter(show_time__date=date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: Optional[datetime.datetime] = None,
        movie_id: Optional[int] = None,
        cinema_hall_id: Optional[int] = None,
) -> QuerySet:
    # I'm not sure if it's legal to go this, but it passes all the tests
    updates = {}
    if show_time:
        updates["show_time"] = show_time
    if movie_id:
        updates["movie_id"] = movie_id
    if cinema_hall_id:
        updates["cinema_hall_id"] = cinema_hall_id

    if updates:
        MovieSession.objects.filter(id=session_id).update(**updates)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
