from __future__ import annotations

from datetime import datetime
from typing import Optional
from django.db.models import QuerySet
from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    movie = Movie.objects.get(pk=movie_id)
    cinema_hall = CinemaHall.objects.get(pk=cinema_hall_id)
    return MovieSession.objects.create(
        movie=movie,
        cinema_hall=cinema_hall,
        show_time=movie_show_time
    )


def get_movies_sessions(session_date: Optional[str] = None) -> QuerySet:
    queryset = MovieSession.objects.all()
    if session_date:
        queryset = queryset.filter(show_time__date=session_date)
    return queryset


def get_movie_session_by_id(movie_session_id: int) -> Optional[MovieSession]:
    try:
        return MovieSession.objects.get(pk=movie_session_id)
    except MovieSession.DoesNotExist:
        return None


def update_movie_session(
        session_id: int,
        show_time: Optional[datetime] = None,
        movie_id: Optional[int] = None,
        cinema_hall_id: Optional[int] = None
) -> Optional[MovieSession]:
    if not any([show_time, movie_id, cinema_hall_id]):
        return None

    movie_session = get_movie_session_by_id(session_id)
    if movie_session is None:
        return None

    if show_time:
        movie_session.show_time = show_time

    if movie_id:
        movie_session.movie = Movie.objects.get(pk=movie_id)

    if cinema_hall_id:
        movie_session.cinema_hall = CinemaHall.objects.get(pk=cinema_hall_id)

    movie_session.save()
    return movie_session


def delete_movie_session_by_id(session_id: int) -> None:
    movie_session = get_movie_session_by_id(session_id)
    if movie_session:
        movie_session.delete()
