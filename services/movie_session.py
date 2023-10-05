from datetime import datetime
from typing import Tuple, Optional

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int

) -> MovieSession:
    new_movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )

    return new_movie_session


def get_movies_sessions(
        session_date: Optional[str] = None
) -> QuerySet[MovieSession]:
    movies_sessions_set = MovieSession.objects.all()

    if session_date is not None:
        movies_sessions_set = movies_sessions_set.filter(
            show_time__date=session_date
        )
    return movies_sessions_set


def get_movie_session_by_id(
        movie_session_id: int
) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: Optional[Tuple[int]] = None,
        movie_id: Optional[int] = None,
        cinema_hall_id: Optional[int] = None
) -> MovieSession:
    select_movie_session = MovieSession.objects.filter(
        id=session_id
    )

    if show_time is not None:
        select_movie_session.update(
            show_time=show_time
        )

    if movie_id is not None:
        select_movie_session.update(
            movie_id=movie_id
        )

    if cinema_hall_id is not None:
        select_movie_session.update(
            cinema_hall_id=cinema_hall_id
        )

    return select_movie_session


def delete_movie_session_by_id(
        session_id: int
) -> None:
    select_session = get_movie_session_by_id(
        movie_session_id=session_id
    )
    select_session.delete()
