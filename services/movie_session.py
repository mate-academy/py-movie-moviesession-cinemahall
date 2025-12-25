from datetime import datetime
from db.models import MovieSession
from django.db.models import QuerySet
from typing import Optional


def create_movie_session(
    movie_show_time: datetime,
    movie_id: int,
    cinema_hall_id: int,
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movies_sessions(
        session_date: Optional[str] = None
) -> QuerySet[MovieSession]:
    queryset = MovieSession.objects.all()

    if session_date:
        queryset = queryset.filter(show_time__date=session_date)

    return queryset


def update_movie_session(
    session_id: int,
    show_time: Optional[str] = None,
    movie_id: Optional[int] = None,
    cinema_hall_id: Optional[int] = None,
) -> None:
    movie_session = MovieSession.objects.filter(id=session_id)
    update_fields = {}

    if show_time is not None:
        update_fields["show_time"] = show_time
    if movie_id is not None:
        update_fields["movie_id"] = movie_id
    if cinema_hall_id is not None:
        update_fields["cinema_hall_id"] = cinema_hall_id

    movie_session.update(**update_fields)


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def delete_movie_session_by_id(session_id: int) -> None:
    movie_session = get_movie_session_by_id(session_id)
    movie_session.delete()
