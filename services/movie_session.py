import datetime
from typing import Union

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
    movie_show_time: datetime.datetime,
    movie_id: int,
    cinema_hall_id: int,
) -> None:

    MovieSession.objects.create(
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id,
        show_time=movie_show_time
    )


def get_movies_sessions(
        session_date: Union[str, None] = None
) -> QuerySet:
    queryset = MovieSession.objects.all()

    if session_date:
        session_date = datetime.datetime.strptime(
            session_date, "%Y-%m-%d"
        )

        queryset = queryset.filter(
            show_time__date=session_date
        )

    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
    session_id: int,
    show_time: Union[datetime.datetime, None] = None,
    movie_id: Union[int, None] = None,
    cinema_hall_id: Union[int, None] = None
) -> None:
    movie_session = MovieSession.objects.filter(id=session_id)
    if show_time:
        movie_session.update(show_time=show_time)
    if movie_id:
        movie_session.update(movie_id=movie_id)
    if cinema_hall_id:
        movie_session.update(cinema_hall_id=cinema_hall_id)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
