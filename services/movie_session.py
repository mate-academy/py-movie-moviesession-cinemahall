import datetime

from db.models import MovieSession
from django.db.models.query import QuerySet


def create_movie_session(
    movie_show_time: datetime.time, movie_id: int, cinema_hall_id: int
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id,
    )


def get_movies_sessions(session_date: str = None) -> QuerySet:
    queryset = MovieSession.objects.all()
    if session_date:
        year, month, day = map(int, session_date.split("-"))
        queryset = queryset.filter(
            show_time__year=year, show_time__month=month, show_time__day=day
        )
    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
    session_id: int,
    show_time: datetime.time = None,
    movie_id: int = None,
    cinema_hall_id: int = None,
) -> None:
    current_func_params = {
        "show_time": show_time,
        "movie_id": movie_id,
        "cinema_hall_id": cinema_hall_id,
    }
    current_func_params = {k: v for k, v in current_func_params.items() if v is not None}
    MovieSession.objects.filter(id=session_id).update(**current_func_params)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
