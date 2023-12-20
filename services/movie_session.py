from datetime import datetime
from typing import Optional

from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from db.models import Movie, CinemaHall, MovieSession


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    movie = get_object_or_404(Movie, id=movie_id)
    cinema_hall = get_object_or_404(CinemaHall, id=cinema_hall_id)

    movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie=movie,
        cinema_hall=cinema_hall
    )

    return movie_session


def get_movies_sessions(
        session_date: Optional[str] = None
) -> QuerySet:
    movie_sessions = MovieSession.objects.all()

    if session_date:
        movie_sessions = movie_sessions.filter(show_time__date=session_date)

    return movie_sessions


def get_movie_session_by_id(movie_session_id: int) -> Optional[MovieSession]:
    return get_object_or_404(MovieSession, id=movie_session_id)


def update_movie_session(
    session_id: int,
    show_time: Optional[datetime] = None,
    movie_id: Optional[int] = None,
    cinema_hall_id: Optional[int] = None
) -> Optional[MovieSession]:
    try:
        movie_session = MovieSession.objects.get(id=session_id)

        if show_time:
            movie_session.show_time = show_time
        if movie_id:
            movie_session.movie_id = movie_id
        if cinema_hall_id:
            movie_session.cinema_hall_id = cinema_hall_id

        movie_session.save()

        return movie_session
    except MovieSession.DoesNotExist:
        return None


def delete_movie_session_by_id(session_id: int) -> bool:
    movie_session = get_movie_session_by_id(session_id)

    if movie_session:
        movie_session.delete()
        return True
    else:
        return False
