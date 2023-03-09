from datetime import datetime

from db.models import MovieSession


def create_movie_session(
    movie_show_time: datetime,
    movie_id: int,
    cinema_hall_id: int
) -> MovieSession:
    new_moviesession = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )
    return new_moviesession


def get_movies_sessions(session_date: str = None) -> list[MovieSession]:
    session_query = MovieSession.objects.all()

    if session_date is not None:
        session_query = session_query.filter(show_time__date=session_date)

    return session_query


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
    session_id: int,
    show_time: datetime = None,
    movie_id: int = None,
    cinema_hall_id: int = None
) -> None:
    session_query = MovieSession.objects.filter(id=session_id)

    if show_time:
        session_query.update(show_time=show_time)
    if movie_id:
        session_query.update(movie=movie_id)
    if cinema_hall_id:
        session_query.update(cinema_hall=cinema_hall_id)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
