from django.db.models import QuerySet

from db.models import MovieSession, Movie, CinemaHall
from datetime import datetime
from typing import Optional


def create_movie_session(movie_show_time: str,
                         movie_id: int,
                         cinema_hall_id: int) -> MovieSession:
    if isinstance(movie_show_time, str):
        movie_show_time = datetime.strptime(
            movie_show_time,
            "%Y-%m-%d %H:%M:%S")

    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)

    movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie=movie,
        cinema_hall=cinema_hall,
    )

    return movie_session


def get_movies_sessions(session_date: Optional[str] = None) -> QuerySet:
    sessions = MovieSession.objects.all()

    if session_date:
        try:
            parsed_date = datetime.strptime(session_date, "%Y-%m-%d").date()
            sessions = sessions.filter(show_time__date=parsed_date)
        except ValueError:
            raise ValueError("Invalid date format. "
                             "Use 'year-month-day' (e.g., '2025-01-13').")

    return sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(
        id=movie_session_id
    )


def update_movie_session(
    session_id: int,
    show_time: Optional[str] = None,
    movie_id: Optional[int] = None,
    cinema_hall_id: Optional[int] = None
) -> MovieSession:
    movie_session = MovieSession.objects.get(id=session_id)

    if show_time:
        if isinstance(show_time, datetime):  # Already a datetime object
            movie_session.show_time = show_time
        else:
            movie_session.show_time = datetime.strptime(
                show_time,
                "%Y-%m-%d %H:%M:%S"
            )

    if movie_id:
        movie_session.movie = Movie.objects.get(id=movie_id)

    if cinema_hall_id:
        movie_session.cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)

    movie_session.save()
    return movie_session


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(pk=session_id).delete()
