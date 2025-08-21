from datetime import datetime
from typing import Optional

from django.db.models import QuerySet

from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int,
) -> MovieSession:
    if isinstance(movie_show_time, str):
        try:
            movie_show_time = (datetime.strptime
                               (movie_show_time,
                                "%Y-%m-%d %H:%M:%S")
                               )
        except ValueError:
            raise TypeError("Movie show time must be in format"
                            " YYYY-MM-DD HH:MM:SS")
    elif not isinstance(movie_show_time, datetime):
        raise TypeError("movie_show_time must be str or datetime")

    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)

    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=cinema_hall,
        movie=movie
    )


def get_movies_sessions(session_date: Optional[str] = None) -> QuerySet:
    if session_date is None:
        return MovieSession.objects.all()
    else:
        return MovieSession.objects.filter(show_time__date=session_date)


def get_movie_session_by_id(movie_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_id)


def update_movie_session(
        session_id: int,
        show_time: Optional[datetime] = None,
        movie_id: Optional[int] = None,
        cinema_hall_id: Optional[int] = None,
) -> MovieSession:

    session = MovieSession.objects.get(id=session_id)

    if show_time is not None:
        session.show_time = show_time

    if movie_id is not None:
        session.movie = Movie.objects.get(id=movie_id)

    if cinema_hall_id is not None:
        session.cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)

    session.save()
    return session


def delete_movie_session_by_id(session_id: int) -> None:
    return MovieSession.objects.filter(id=session_id).delete()
