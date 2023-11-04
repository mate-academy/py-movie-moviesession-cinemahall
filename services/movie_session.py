from datetime import datetime
from django.db.models.query import QuerySet

from db.models import MovieSession


def create_movie_session(
    movie_show_time: datetime,
    movie_id: int,
    cinema_hall_id: int
) -> MovieSession:
    new_session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )

    return new_session


def get_movies_sessions(
    session_date: str = None,
) -> QuerySet:
    queryset = MovieSession.objects.all()

    if session_date:
        queryset = queryset.filter(show_time__date=session_date)

    return queryset


def get_movie_session_by_id(
    movie_session_id: int
) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
    session_id: int,
    show_time: datetime = None,
    movie_id: int = None,
    cinema_hall_id: int = None
) -> MovieSession:
    movie = MovieSession.objects.get(id=session_id)

    if show_time is not None:
        movie.show_time = show_time
        movie.save()

    if movie_id is not None:
        movie.movie_id = movie_id
        movie.save()

    if cinema_hall_id is not None:
        movie.cinema_hall_id = cinema_hall_id
        movie.save()

    return movie


def delete_movie_session_by_id(session_id: int) -> None:
    movie_to_delete = MovieSession.objects.get(id=session_id)
    movie_to_delete.delete()
