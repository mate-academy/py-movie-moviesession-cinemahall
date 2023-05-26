from django.db.models import QuerySet

from db.models import MovieSession
from typing import Optional


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movies_sessions(session_date: Optional[str] = None) -> QuerySet:
    queryset = MovieSession.objects.all()

    if session_date:
        queryset = queryset.filter(show_time__date=session_date)

    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: Optional[int],
        show_time: Optional[str] = None,
        movie_id: Optional[int] = None,
        cinema_hall_id: int = None
) -> None:
    update_params = {
        field_name: field_value
        for field_name, field_value in {
            "show_time": show_time,
            "movie_id": movie_id,
            "cinema_hall_id": cinema_hall_id
        }.items()
        if field_value is not None
    }

    if update_params:
        MovieSession.objects.filter(id=session_id).update(**update_params)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
