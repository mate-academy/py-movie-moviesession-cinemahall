from db.models import MovieSession, Movie, CinemaHall

from django.db.models import QuerySet
from datetime import datetime


def create_movie_session(
    movie_show_time: datetime, movie_id: int, cinema_hall_id: int
) -> None:
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    movie = Movie.objects.get(id=movie_id)
    MovieSession.objects.create(
        show_time=movie_show_time, movie=movie, cinema_hall=cinema_hall
    )


def get_movies_sessions(session_date: str = None) -> QuerySet[MovieSession]:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
    session_id: int,
    show_time: datetime | None = None,
    movie_id: int | None = None,
    cinema_hall_id: int | None = None,
) -> None:
    session = get_movie_session_by_id(session_id)
    if show_time is not None:
        session.show_time = show_time
    if movie_id is not None:
        session.movie = movie_id
    if cinema_hall_id is not None:
        session.cinema_hall = cinema_hall_id
    session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    get_movie_session_by_id(session_id).delete()
