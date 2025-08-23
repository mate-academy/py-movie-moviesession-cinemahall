from db.models import MovieSession, Movie, CinemaHall
from django.core.exceptions import ObjectDoesNotExist
from typing import Optional
import datetime
from django.db.models.query import QuerySet


def create_movie_session(
        movie_show_time: datetime.datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)

    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie=movie,
        cinema_hall=cinema_hall
    )


def get_movie_session(
    session_date: Optional[str] = None
) -> QuerySet[MovieSession]:
    qs = MovieSession.objects.all()
    if session_date:
        qs = qs.filter(show_time__date=session_date)
    return qs


def get_movie_sessions_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.filter(id=movie_session_id)


def update_movie_session(
    session_id: int,
    show_time: Optional[datetime.datetime] = None,
    movie_id: Optional[int] = None,
    cinema_hall_id: Optional[int] = None
) -> MovieSession:
    session = MovieSession.objects.get(id=session_id)
    if show_time:
        session.show_time = show_time
    if movie_id:
        session.movie = Movie.objects.get(id=movie_id)
    if cinema_hall_id:
        session.cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    session.save()
    return session


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
