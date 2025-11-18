import init_django_orm  # noqa: F401

from datetime import datetime
from django.db.models.query import QuerySet
from db.models import CinemaHall, MovieSession, Movie


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=CinemaHall.objects.get(id=cinema_hall_id),
        movie=Movie.objects.get(id=movie_id)
    )


def get_movies_sessions(session_date: str = "") -> QuerySet:
    sessions = MovieSession.objects.all()
    if session_date:
        date = datetime.strptime(session_date, "%Y-%m-%d").date()
        sessions = sessions.filter(show_time__date=date)
    return sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime | None = None,
        movie_id: int = -1,
        cinema_hall_id: int = -1
) -> None:
    session = MovieSession.objects.get(id=session_id)

    if show_time:
        session.show_time = show_time

    if movie_id > -1:
        session.movie = Movie.objects.get(id=movie_id)
    if cinema_hall_id > -1:
        session.cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)

    session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    session = MovieSession.objects.get(id=session_id)
    session.delete()
