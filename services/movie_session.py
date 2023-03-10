from datetime import datetime

from django.db.models.query import QuerySet

from db.models import CinemaHall, Movie, MovieSession


def create_movie_session(
    movie_show_time: datetime,
    movie_id: int,
    cinema_hall_id: int,
) -> None:

    MovieSession.objects.create(
        show_time=movie_show_time,
        movie=Movie.objects.get(id=movie_id),
        cinema_hall=CinemaHall.objects.get(id=cinema_hall_id),
    )


def get_movies_sessions(session_date: str = "") -> "QuerySet":
    movies_sessions = MovieSession.objects.all()

    if session_date:
        movies_sessions = movies_sessions.filter(show_time__date=session_date)

    return movies_sessions


def get_movie_session_by_id(movie_session_id: int) -> object:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
    session_id: int,
    show_time: datetime = None,  # type: ignore
    cinema_hall_id: int = 0,
    movie_id: int = 0
) -> None:

    appropriate_movie = MovieSession.objects.filter(id=session_id)

    if show_time:
        appropriate_movie.update(show_time=show_time)
    if cinema_hall_id:
        appropriate_movie.update(cinema_hall=cinema_hall_id)
    if movie_id:
        appropriate_movie.update(movie=movie_id)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
