from typing import Any

from db.models import MovieSession


def create_movie_session(
        movie_show_time: float,
        movie_id: int,
        cinema_hall_id: int
        ) -> MovieSession:

    new_movie_session = MovieSession.objects.create(
        movie_show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
        )

    return new_movie_session


def get_movies_sessions(session_date: str) -> Any:
    queryset = MovieSession.objects.all()

    if session_date:
        return queryset.filter(show_time__date=session_date)
    return queryset


def get_movie_session_by_id(movie_session_id: int) -> None:
    return MovieSession.objects.all().filter(
        movie_session_id=movie_session_id
    )


def update_movie_session(
        session_id: int,
        show_time: float = None,
        movie_id: int = None,
        cinema_hall_id: int = None
        ) -> None:

    queryset = MovieSession.objects.filter(id=session_id)
    if show_time:
        queryset = queryset.update(show_time=show_time)
    if movie_id:
        queryset = queryset.update(movie_id=movie_id)
    if cinema_hall_id:
        queryset = queryset.update(cinema_hall_id=cinema_hall_id)

    return queryset


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
