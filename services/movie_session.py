from datetime import datetime
from typing import Optional

from django.db.models import QuerySet

from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int
                         ) -> MovieSession:
    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    movie_session = MovieSession.objects.create(
        movie=movie,
        cinema_hall=cinema_hall,
        show_time=movie_show_time
    )
    return movie_session

def get_movie_session(session_date: Optional[str] = None) -> QuerySet:
    if session_date:
        return MovieSession.objects.filter(show_time=session_date)
    return MovieSession.objects.all()

def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)

def update_movie_session(session_id: int,
                         show_time: Optional[datetime] = None,
                         movie_id: Optional[int] = None,
                         cinema_hall_id: Optional[int] = None
                         ) -> None:
    movie_session = MovieSession.objects.get(id=session_id)
    if show_time:
        movie_session.show_time = show_time
    if movie_id:
        movie_session.movie_id = movie_id
    if cinema_hall_id:
        movie_session.cinema_hall_id = cinema_hall_id
    movie_session.save()

def delete_movie_session_by_id(session_id: int) -> None:
    movie_session = MovieSession.objects.get(id=session_id)
    movie_session.delete()
