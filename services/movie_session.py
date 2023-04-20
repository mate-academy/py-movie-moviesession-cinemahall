from typing import Any
from db.models import Movie, MovieSession, CinemaHall
from django.core.exceptions import ObjectDoesNotExist


def create_movie_session(
        movie_show_time: str,
        cinema_hall_id: int,
        movie_id: int
) -> Any:
    cinema_hall = None
    movie = None

    try:
        cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
        movie = Movie.objects.get(id=movie_id)
    except ObjectDoesNotExist as error:
        print(error)

    movie_session, _ = MovieSession.objects.get_or_create(
        show_time=movie_show_time,
        cinema_hall=cinema_hall,
        movie=movie,
    )


def get_movies_sessions(session_date: str = None) -> MovieSession:
    movie_sessions = MovieSession.objects.all()
    if session_date:
        movie_sessions = movie_sessions.filter(show_time__date=session_date)
    return movie_sessions


def get_movie_session_by_id(movie_session_id: int) -> Any:
    try:
        return MovieSession.objects.get(id=movie_session_id)
    except ObjectDoesNotExist as error:
        return error


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:

    movie_session = get_movie_session_by_id(session_id)

    if show_time:
        movie_session.show_time = show_time
    if movie_id:
        movie = Movie.objects.get(id=movie_id)
        movie_session.movie = movie
    if cinema_hall_id:
        cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
        movie_session.cinema_hall = cinema_hall
    movie_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    movie_session = get_movie_session_by_id(session_id)
    movie_session.delete()
