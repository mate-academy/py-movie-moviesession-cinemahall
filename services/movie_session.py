from django.db.models import QuerySet
from db.models import MovieSession
from typing import Any


def create_movie_session(
        movie_show_time: Any,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    MovieSession.objects.get_or_create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id,
    )


def get_movies_sessions(session_date: str = None) -> QuerySet:
    queryset = MovieSession.objects.all()

    if session_date:
        queryset = queryset.filter(show_time__date=session_date)

    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int = None,
        show_time: str = None,
        movie_id: str = None,
        cinema_hall_id: str = None,
) -> None:

    movie_session = MovieSession.objects.get(id=session_id)

    if movie_id:
        movie_session.movie_id = movie_id  # Corrected indentation

    if cinema_hall_id:
        movie_session.cinema_hall_id = cinema_hall_id

    if show_time:
        movie_session.show_time = show_time

    movie_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    movie_session = MovieSession.objects.get(id=session_id)
    movie_session.delete()
