from db.models import MovieSession
from datetime import time
from django.db.models import QuerySet


def create_movie_session(
        movie_show_time: time,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movie_session_by_id(
        movie_session_id: int
) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def get_movies_sessions(
        session_date: str = None
) -> QuerySet[MovieSession]:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def update_movie_session(
        session_id: int,
        show_time: time = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    data = {}
    for key, value in {
        "show_time": show_time,
        "movie_id": movie_id,
        "cinema_hall_id": cinema_hall_id
    }.items():
        if value is not None:
            data[key] = value
    MovieSession.objects.filter(pk=session_id).update(**data)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(pk=session_id).delete()
