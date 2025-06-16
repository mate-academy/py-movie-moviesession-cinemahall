from datetime import datetime
from typing import Optional
from django.db.models.query import QuerySet
from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    session = MovieSession.objects.create(show_time=movie_show_time,
                                          movie=movie, cinema_hall=cinema_hall)
    return session


def get_movies_sessions(session_date: Optional[str] = None) -> QuerySet:
    qs = MovieSession.objects.all()
    if session_date:
        qs = qs.filter(show_time__date=session_date)
    return qs


def get_movie_session_by_id(movie_session_id: int) -> Optional[MovieSession]:
    return MovieSession.objects.filter(id=movie_session_id).first()


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> Optional[MovieSession]:

    session = MovieSession.objects.filter(id=session_id).first()
    if not session:
        return None

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
