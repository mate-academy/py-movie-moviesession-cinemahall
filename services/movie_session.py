from db.models import CinemaHall, Genre, Actor, Movie, MovieSession
from django.db.models import QuerySet
import datetime


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id = int,
) -> None:
    MovieSession.objects.create(
        movie_id=movie_id,
        show_time=movie_show_time,
        cinema_hall=cinema_hall_id,
    )


def get_movies_sessions(session_date: str) -> QuerySet:
    pass


def get_movie_session_by_id() -> QuerySet:
    pass


def update_movie_session() -> None:
    pass


def delete_movie_session() -> None:
    pass