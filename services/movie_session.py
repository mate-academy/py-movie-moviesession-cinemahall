from django.db.models import QuerySet
import datetime
from db.models import MovieSession
from typing import Optional


def create_movie_session(movie_show_time: datetime, movie_id: int,
                         cinema_hall_id: int) -> MovieSession:
    movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id,
    )
    return movie_session


def get_movies_sessions(session_date: Optional[str] = None) -> QuerySet:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    else:
        return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    movie_session = MovieSession.objects.get(id=movie_session_id)
    return movie_session


def update_movie_session(
    session_id: int,
    show_time: Optional[datetime] = None,
    movie_id: Optional[int] = None,
    cinema_hall_id: Optional[int] = None,
) -> MovieSession:

    instance = MovieSession.objects.get(id=session_id)

    updated_fields = []
    if show_time is not None:
        instance.show_time = show_time
        updated_fields.append("show_time")
    if movie_id is not None:
        instance.movie_id = movie_id
        updated_fields.append("movie_id")
    if cinema_hall_id is not None:
        instance.cinema_hall_id = cinema_hall_id
        updated_fields.append("cinema_hall_id")

    if updated_fields:
        instance.save(update_fields=updated_fields)

    return instance


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
