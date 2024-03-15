from db.models import MovieSession, CinemaHall, Movie
from django.db.models import QuerySet
from datetime import datetime


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    movie = Movie.objects.get(id=movie_id)
    new_movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=cinema_hall,
        movie=movie
    )
    return new_movie_session


def get_movies_sessions(session_date: datetime | None = None) -> QuerySet:
    movies_sessions = MovieSession.objects.all()
    if session_date:
        movies_sessions = movies_sessions.filter(show_time__date=session_date)
    return movies_sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime | None = None,
        movie_id: int | None = None,
        cinema_hall_id: int | None = None
) -> MovieSession:
    movie_session = MovieSession.objects.get(id=session_id)
    if show_time:
        movie_session.show_time = show_time
    if movie_id:
        movie_session.movie_id = movie_id
    if cinema_hall_id:
        movie_session.cinema_hall_id = cinema_hall_id
    movie_session.save()
    return movie_session


def delete_movie_session_by_id(session_id: int) -> None:
    movie_session = MovieSession.objects.get(id=session_id)
    movie_session.delete()
