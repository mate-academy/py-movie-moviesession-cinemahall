from typing import Any

from db.models import MovieSession


def create_movie_session(
        movie_show_time: Any,
        movie_id: int,
        cinema_hall_id: int
) -> Any:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(session_date: str = None) -> Any:
    queryset = MovieSession.objects.all()

    if session_date:
        queryset = queryset.filter(show_time__date=session_date)

    return queryset


def get_movie_session_by_id(movie_session_id: int) -> Any:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: Any = None,
        movie_id: Any = None,
        cinema_hall_id: Any = None
) -> Any:
    session = MovieSession.objects.get(id=session_id)

    if show_time:
        session.show_time = show_time
    if movie_id:
        session.movie_id = movie_id
    if cinema_hall_id:
        session.cinema_hall_id = cinema_hall_id

    session.save()
    return session


def delete_movie_session_by_id(session_id: int) -> Any:
    MovieSession.objects.get(id=session_id).delete()
