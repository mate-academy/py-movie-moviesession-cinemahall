from typing import Optional, Union

from django.db.models import QuerySet

from db.models import MovieSession, Movie, CinemaHall
import datetime


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int
                         ) -> MovieSession:
    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=cinema_hall,
        movie=movie
    )


def get_movies_sessions(
        session_date: Optional[Union[datetime, str]] = None)\
        -> QuerySet[MovieSession]:
    if not session_date:
        return MovieSession.objects.all()
    year, month, day = map(int, session_date.split("-"))
    movies = MovieSession.objects.filter(
        show_time__date=datetime.date(year=int(year),
                                      month=int(month),
                                      day=int(day)))
    return movies


def get_movie_session_by_id(
        movie_session_id: int) -> MovieSession | QuerySet[MovieSession]:
    return MovieSession.objects.filter(id=movie_session_id).first()


def update_movie_session(session_id: int,
                         show_time: datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None
                         ) -> MovieSession:
    session = MovieSession.objects.get(id=session_id)

    if show_time:
        session.show_time = show_time

    if movie_id:
        movie_obj = Movie.objects.get(id=movie_id)
        session.movie = movie_obj

    if cinema_hall_id:
        cinema_hall_obj = CinemaHall.objects.get(id=cinema_hall_id)
        session.cinema_hall = cinema_hall_obj

    session.save()
    return session


def delete_movie_session_by_id(session_id: int) -> None:
    session = MovieSession.objects.get(id=session_id)
    session.delete()
