from typing import Optional

from django.db.models import QuerySet

from db.models import CinemaHall, Movie, MovieSession


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    movie = Movie.objects.get(id=movie_id)

    new_movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie=movie,
        cinema_hall=cinema_hall
    )

    return new_movie_session


def get_movies_sessions(
        session_date: Optional[str] = None
) -> QuerySet[MovieSession]:
    session = MovieSession.objects.all()
    if session_date:
        session = session.filter(show_time__date=session_date)

    return session


def get_movie_session_by_id(
        movie_session_id: int
) -> QuerySet[MovieSession]:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: Optional[int] = None,
        movie_id: Optional[int] = None,
        cinema_hall_id: Optional[int] = None,
) -> None:
    session_to_update = MovieSession.objects.filter(id=session_id)
    if show_time:
        session_to_update.update(show_time=show_time)
    if movie_id:
        session_to_update.update(movie_id=movie_id)
    if cinema_hall_id:
        session_to_update.update(cinema_hall_id=cinema_hall_id)


def delete_movie_session_by_id(session_id: int) -> None:
    return get_movie_session_by_id(session_id).delete()
