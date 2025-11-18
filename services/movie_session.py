from datetime import datetime
from typing import Optional

from django.db.models import QuerySet
from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(
    movie_show_time: datetime,
    movie_id: int,
    cinema_hall_id: int,
) -> MovieSession:
    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie=movie,
        cinema_hall=cinema_hall,
    )
    return movie_session


def get_movies_sessions(
    session_date: str | None = None,
) -> QuerySet[MovieSession]:
    movie_sessions = MovieSession.objects.all()

    if session_date:
        movie_sessions = movie_sessions.filter(show_time__date=session_date)

    return movie_sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
    session_id: int,
    show_time: Optional[datetime] = None,
    movie_id: int | None = None,
    cinema_hall_id: int | None = None,
) -> MovieSession:
    movie_session = MovieSession.objects.get(id=session_id)

    if show_time is not None:
        movie_session.show_time = show_time

    if movie_id is not None:
        movie_session.movie = Movie.objects.get(id=movie_id)

    if cinema_hall_id is not None:
        movie_session.cinema_hall = CinemaHall.objects.get(
            id=cinema_hall_id,
        )

    movie_session.save()
    return movie_session


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
