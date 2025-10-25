import datetime
from typing import Optional

from django.db.models import QuerySet

from db.models import MovieSession


def _to_naive_utc(
        dt: Optional[datetime.datetime]
) -> Optional[datetime.datetime]:

    if dt is None:
        return None
    if dt.tzinfo is not None:
        dt = dt.astimezone(datetime.timezone.utc).replace(tzinfo=None)
    return dt


def create_movie_session(
        movie_show_time: datetime.datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:

    movie_session = MovieSession.objects.create(
        show_time=_to_naive_utc(movie_show_time),
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )
    return movie_session


def get_movies_sessions(
        session_date: Optional[str] = None
) -> QuerySet[MovieSession]:

    if session_date is None:
        return MovieSession.objects.all()
    parsed_date = datetime.datetime.strptime(session_date, "%Y-%m-%d").date()
    return MovieSession.objects.filter(show_time__date=parsed_date)


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: Optional[datetime.datetime] = None,
        movie_id: Optional[int] = None,
        cinema_hall_id: Optional[int] = None
) -> MovieSession:

    movie_session = MovieSession.objects.get(id=session_id)

    if show_time is not None:
        movie_session.show_time = _to_naive_utc(show_time)
    if movie_id is not None:
        movie_session.movie_id = movie_id
    if cinema_hall_id is not None:
        movie_session.cinema_hall_id = cinema_hall_id
    movie_session.save()
    return movie_session


def delete_movie_session_by_id(session_id: int) -> None:
    movie_session = MovieSession.objects.get(id=session_id)
    movie_session.delete()
