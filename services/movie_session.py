from django.db.models.query import QuerySet

from db.models import MovieSession, Movie, CinemaHall
from datetime import datetime


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int,
) -> MovieSession:
    movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id,
    )
    return movie_session


def get_movies_sessions(
        session_date: str=None,
) -> QuerySet:
    if session_date:
        date=datetime.strptime(session_date, "%Y-%m-%d").date()
        return MovieSession.objects.filter(show_time__date = date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.filter(id=movie_session_id).first()


def update_movie_session(session_id: int, **kwargs) -> bool:
    updated = MovieSession.objects.filter(id=session_id).update(**kwargs)
    return updated > 0


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
