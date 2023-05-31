from datetime import datetime
from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(session_date: datetime = None) -> QuerySet:
    queryset = MovieSession.objects.all()
    if session_date:
        queryset = queryset.filter(show_time__date=session_date)
    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    movie_session_update = get_object_or_404(MovieSession, id=session_id)
    if show_time:
        movie_session_update.show_time = show_time
    if movie_id:
        movie_session_update.movie_id = movie_id
    if cinema_hall_id:
        movie_session_update.cinema_hall_id = cinema_hall_id
    movie_session_update.save()


def delete_movie_session_by_id(session_id: int) -> None:
    delete_movie = get_object_or_404(MovieSession, id=session_id)
    delete_movie.delete()
