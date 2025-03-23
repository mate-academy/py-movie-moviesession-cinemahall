from django.db.models import QuerySet

from db.models import CinemaHall, Movie, MovieSession
from datetime import datetime


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie=Movie.objects.get(id=movie_id),
        cinema_hall=CinemaHall.objects.get(id=cinema_hall_id)
    )


def get_movies_sessions(session_date: str = None) -> (
        QuerySet[MovieSession] | None):
    if session_date is None:
        return MovieSession.objects.all()
    if session_date is not None:
        date = datetime.strptime(session_date, "%Y-%m-%d")
        return MovieSession.objects.filter(show_time__date=date)


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> None:
    query = MovieSession.objects.get(id=session_id)
    if show_time is not None:
        query.show_time = show_time
    if movie_id is not None:
        query.movie_id = movie_id
    if cinema_hall_id is not None:
        query.cinema_hall_id = cinema_hall_id
    query.save()


def delete_movie_session_by_id(session_id: int) -> None:
    query = MovieSession.objects.get(id=session_id)
    query.delete()
