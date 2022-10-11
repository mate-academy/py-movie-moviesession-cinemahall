from datetime import datetime

from db.models import MovieSession


def create_movie_session(movie_show_time: datetime,
                         movie_id: int, cinema_hall_id: int) -> str:
    new_session = MovieSession.objects.create(
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id,
        show_time=movie_show_time
    )

    return new_session


def get_movies_sessions(session_date: datetime = None) -> str:
    queryset = MovieSession.objects.all()

    if session_date is not None:
        queryset.filter(show_time__date=session_date)

    return queryset


def get_movie_session_by_id(movie_session_id: int) -> str:
    return MovieSession.objects.filter(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> str:
    session = MovieSession.objects.filter(id=session_id)

    if show_time is not None:
        session.update(show_time=show_time)
    if movie_id is not None:
        session.update(movie_id=movie_id)
    if cinema_hall_id is not None:
        session.update(cinema_hall_id=cinema_hall_id)

    return session


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
