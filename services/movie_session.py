from django.db.models import QuerySet

from db.models import MovieSession
import datetime
from typing import Optional


def create_movie_session(movie_show_time: datetime.datetime,
                         movie_id: int,
                         cinema_hall_id: int
                         ) -> MovieSession:
    movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id,
    )

    return movie_session


def _parse_flexible_date(date_str: str) -> datetime.date:
    """
    Return YYYY-MM-DD
    """
    parts = date_str.split("-")
    if len(parts) != 3:
        raise ValueError(f"Invalid date: {date_str}")
    year, month, day = map(int, parts)
    return datetime.date(year, month, day)


def get_movies_sessions(session_date: Optional[str] = None
                        ) -> QuerySet[MovieSession]:
    """
    session_date: рядок "YYYY-MM-DD" або None.
    """
    queryset = MovieSession.objects.all()
    if session_date:
        date_obj = _parse_flexible_date(session_date)
        queryset = queryset.filter(show_time__date=date_obj)
    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: Optional[datetime.datetime] = None,
                         movie_id: Optional[int] = None,
                         cinema_hall_id: Optional[int] = None) -> MovieSession:
    movie_session = MovieSession.objects.get(id=session_id)

    if show_time is not None:
        movie_session.show_time = show_time
    if movie_id is not None:
        movie_session.movie_id = movie_id
    if cinema_hall_id is not None:
        movie_session.cinema_hall_id = cinema_hall_id

    movie_session.save()
    return movie_session


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
