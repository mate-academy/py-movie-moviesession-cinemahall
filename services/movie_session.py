from db.models import MovieSession
from datetime import datetime as dt
from services.movie import get_movie_by_id
from services.cinema_hall import get_cinema_halls_by_id


def create_movie_session(
        movie_show_time: dt,
        movie_id: int,
        cinema_hall_id: int
) -> None:

    hall = get_cinema_halls_by_id(cinema_hall_id)
    movie = get_movie_by_id(movie_id)
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=hall,
        movie=movie
    )


def get_movies_sessions(session_date: str = None) -> list[MovieSession]:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date).all()
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:

    session = get_movie_session_by_id(session_id)
    if show_time:
        session.show_time = show_time

    if movie_id:
        movie_id = get_movie_by_id(movie_id)
        session.movie = movie_id

    if cinema_hall_id:
        cinema_hall_id = get_cinema_halls_by_id(cinema_hall_id)
        session.cinema_hall = cinema_hall_id
    session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    get_movie_session_by_id(session_id).delete()
