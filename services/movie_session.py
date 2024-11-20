from datetime import datetime

from django.db.models import QuerySet

from db.models import MovieSession, Movie, CinemaHall
from tests.test_main import movie_session_database_data


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    movie_to_create = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=cinema_hall,
        movie=movie
    )
    return movie_to_create


def get_movies_sessions(
        session_date: str = None
) -> QuerySet[MovieSession]:
    queryset = MovieSession.objects.all()

    if session_date:
        queryset = queryset.filter(show_time__in=session_date)

    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> MovieSession:
    movie_session = MovieSession.objects.get(id=session_id)

    if show_time:
        movie_session.show_time=show_time

    if movie_id:
        movie_session.movie_id=movie_id

    if cinema_hall_id:
        movie_session.cinema_hall_id=cinema_hall_id

    return movie_session


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()