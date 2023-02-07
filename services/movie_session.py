from db.models import MovieSession
from django.db.models import QuerySet
import datetime


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id,
    )


def get_movies_sessions(session_date: datetime = None) -> QuerySet:
    queryset = MovieSession.objects.all()
    if session_date:
        return queryset.filter(show_time__date=session_date)
    return queryset


def get_movie_session_by_id(movie_session_id: int) -> object:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    upd_movie = MovieSession.objects.filter(id=session_id)

    if show_time:
        upd_movie.update(show_time=show_time)

    if movie_id:
        upd_movie.update(movie_id=movie_id)

    if cinema_hall_id:
        upd_movie.update(cinema_hall_id=cinema_hall_id)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
