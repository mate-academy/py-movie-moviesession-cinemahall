from datetime import datetime
from typing import Optional, cast

from django.db.models import QuerySet

from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int, ) -> MovieSession:
    movie = Movie.objects.get(pk=movie_id)
    cinema_hall = CinemaHall.objects.get(pk=cinema_hall_id)

    return MovieSession.objects.create(show_time=movie_show_time,
                                       cinema_hall=cinema_hall,
                                       movie=movie)


def get_movies_sessions(
        session_date: Optional[str] = None) -> QuerySet[MovieSession]:
    if session_date:
        return cast(QuerySet[MovieSession],
                    MovieSession.objects.filter(show_time__date=session_date))
    else:
        return cast(QuerySet[MovieSession], MovieSession.objects.all())


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return cast(MovieSession, MovieSession.objects.get(pk=movie_session_id))


def update_movie_session(session_id: int,
                         show_time: Optional[datetime] = None,
                         movie_id: Optional[int] = None,
                         cinema_hall_id: Optional[int] = None) -> MovieSession:
    session = MovieSession.objects.get(pk=session_id)
    if show_time is not None:
        session.show_time = show_time

    if movie_id is not None:
        session.movie_id = movie_id

    if cinema_hall_id is not None:
        session.cinema_hall = CinemaHall.objects.get(pk=cinema_hall_id)

    session.save()
    return session


def delete_movie_session_by_id(session_id: int) -> None:
    session = MovieSession.objects.get(pk=session_id)
    session.delete()
