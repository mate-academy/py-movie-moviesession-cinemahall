from __future__ import annotations

from datetime import datetime
from typing import Optional
from django.db.models import QuerySet
from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(
        movie_show_time: datetime,
        movie: Movie,
        cinema_hall: CinemaHall
) -> MovieSession:
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
        movie: Optional[Movie] = None,
        cinema_hall: Optional[CinemaHall] = None
) -> Optional[MovieSession]:
    if not any([show_time, movie, cinema_hall]):
        return None

    movie_session = get_movie_session_by_id(session_id)
    if movie_session is None:
        return None

    if show_time:
        movie_session.show_time = show_time

    if movie:
        movie_session.movie = movie

    if cinema_hall:
        movie_session.cinema_hall = cinema_hall

    movie_session.save()
    return movie_session



def delete_movie_session_by_id(session_id: int) -> None:
    movie_session = get_movie_session_by_id(session_id)
    if movie_session:
        movie_session.delete()
