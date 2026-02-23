from typing import Optional
from datetime import datetime, date

from django.db.models import QuerySet

from db.models import MovieSession, CinemaHall, Movie


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=CinemaHall.objects.get(id=cinema_hall_id),
        movie=Movie.objects.get(id=movie_id)
    )


def get_movies_sessions(
        session_date: Optional[date] = None
) -> QuerySet:
    if session_date is not None:
        return MovieSession.objects.filter(show_time__date=session_date)
    else:
        return MovieSession.objects.all()


def get_movie_session_by_id(
        movie_session_id: int
) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: Optional[datetime] = None,
        movie_id: Optional[int] = None,
        cinema_hall_id: Optional[int] = None
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


def delete_movie_session_by_id(
        session_id: int
) -> None:
    MovieSession.objects.get(id=session_id).delete()
