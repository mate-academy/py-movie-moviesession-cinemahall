from datetime import datetime

from django.db.models import QuerySet

from db.models import MovieSession, Movie, CinemaHall
from services.serv_support import (
    is_date_correct, is_table_item_exist
)


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> MovieSession:
    if (isinstance(movie_show_time, datetime)
            and is_table_item_exist(Movie, movie_id)
            and is_table_item_exist(CinemaHall, cinema_hall_id)):
        return MovieSession.objects.create(
            show_time=movie_show_time,
            cinema_hall=CinemaHall.objects.get(id=cinema_hall_id),
            movie=Movie.objects.get(id=movie_id)
        )


def get_movies_sessions(session_date: str | None = None) -> QuerySet:
    query = MovieSession.objects.all()
    if is_date_correct(session_date):
        query = query.filter(show_time__date=session_date)
    return query


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: datetime | None = None,
                         movie_id: int | None = None,
                         cinema_hall_id: int | None = None) -> MovieSession:
    if is_table_item_exist(MovieSession, session_id):
        session = MovieSession.objects.get(id=session_id)
        if isinstance(show_time, datetime):
            session.show_time = show_time
        if is_table_item_exist(Movie, movie_id):
            session.movie = Movie.objects.get(id=movie_id)
        if is_table_item_exist(CinemaHall, cinema_hall_id):
            session.cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
        session.save()
        return session


def delete_movie_session_by_id(session_id: int) -> None:
    if is_table_item_exist(MovieSession, item_id=session_id):
        obj = MovieSession.objects.get(id=session_id)
        obj.delete()
