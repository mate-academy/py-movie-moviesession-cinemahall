from django.db.models import QuerySet

from db.models import MovieSession, Movie, CinemaHall
from datetime import datetime
from typing import List, Optional


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    return MovieSession.objects.create(
        movie=movie,
        cinema_hall=cinema_hall,
        show_time=movie_show_time
    )


def get_movies_sessions(
        session_date: Optional[str] = None
        ) -> QuerySet[MovieSession]:
    qs = MovieSession.objects.all()
    if session_date:
        qs = qs.filter(show_time__date=session_date)
    return qs


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: Optional[datetime] = None,
                         movie_id: Optional[int] = None,
                         cinema_hall_id: Optional[int] = None
                         ) -> MovieSession:

    session = MovieSession.objects.get(id=session_id)

    if show_time:
        session.show_time = show_time

    if movie_id:
        movie = Movie.objects.get(id=movie_id)
        session.movie = movie

    if cinema_hall_id:
        hall = CinemaHall.objects.get(id=cinema_hall_id)
        session.cinema_hall = hall


    session.save()
    return session



def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()

