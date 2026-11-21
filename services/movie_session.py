from db.models import MovieSession
from typing import Any


def create_movie_session(movie_show_time: Any, movie_id: int,
                         cinema_hall_id: int) -> Any:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movies_sessions(session_date: str | None = None) -> Any:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> Any:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
    session_id: int,
    show_time: Any | None = None,
    movie_id: int | None = None,
    cinema_hall_id: int | None = None
) -> Any:
    movie_session = MovieSession.objects.get(id=session_id)
    if show_time is not None:
        movie_session.show_time = show_time
    if cinema_hall_id is not None:
        movie_session.cinema_hall_id = cinema_hall_id
    if movie_id is not None:
        movie_session.movie_id = movie_id
    movie_session.save()
    return movie_session


def delete_movie_session_by_id(session_id: int) -> Any:
    movie_session = MovieSession.objects.get(id=session_id)
    movie_session.delete()
