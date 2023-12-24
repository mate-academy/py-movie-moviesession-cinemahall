from db.models import MovieSession
from django.db.models import QuerySet

import time
import datetime


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    new_movie_session = MovieSession(
        show_time=movie_show_time,
        cinema_hall=cinema_hall_id,
        movie=movie_id
    )

    return new_movie_session


def get_movies_sessions(
    session_date: str = None
) -> QuerySet:
    queryset = MovieSession.objects.all()

    if session_date is not None:
        time_set = time.strptime(f"{session_date}", "%Y-%m-%d")
        queryset = queryset.filter(
            show_time__date__in=time_set
        )
    return queryset


def get_movie_session_by_id(
        movie_session_id: int
) -> MovieSession:
    return MovieSession.objects.get(
        id=movie_session_id
    )


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    new_movie_session = MovieSession.objects.create(
        id=session_id
    )

    if show_time:
        time_set = time.strptime(f"{show_time}", "%Y-%m-%d")
        new_movie_session.show_time.set(time_set)

    if movie_id:
        new_movie_session.movie.set(movie_id)

    if cinema_hall_id:
        new_movie_session.cinema_hall.set(
            cinema_hall_id
        )


def delete_movie_session_by_id(
        session_id: int
) -> None:
    MovieSession.objects.filter(
        id=session_id
    ).delete()
