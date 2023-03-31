from db.models import MovieSession
from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from typing import Optional


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    new_movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )
    return new_movie_session


def get_movies_sessions(session_date: Optional[str] = None) -> QuerySet:
    scheduled_movies = MovieSession.objects.all()
    if session_date is not None:
        scheduled_movies = scheduled_movies.filter(
            show_time__date=session_date
        )
    return scheduled_movies


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    movies_by_session = get_object_or_404(MovieSession, id=movie_session_id)
    return movies_by_session


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: Optional[int] = None,
        cinema_hall_id: Optional[int] = None) -> None:
    movies_by_session = get_movie_session_by_id(session_id)
    if show_time:
        movies_by_session.show_time = show_time
    if movie_id:
        movies_by_session.movie_id = movie_id
    if cinema_hall_id:
        movies_by_session.cinema_hall_id = cinema_hall_id
    movies_by_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    get_movie_session_by_id(session_id).delete()
