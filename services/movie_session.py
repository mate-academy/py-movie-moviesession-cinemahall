from datetime import date
from typing import Optional

from django.db.models import QuerySet

from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)

    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie=movie,
        cinema_hall=cinema_hall
    )


def get_movies_sessions(
        session_date: Optional[date] = None
) -> QuerySet[MovieSession]:

    movie_sessions = MovieSession.objects.all()

    if session_date:
        movie_sessions = movie_sessions.filter(show_time__date=session_date)

    return movie_sessions


def get_movie_session_by_id(movie_session_id: int) -> Optional[MovieSession]:
    try:
        return MovieSession.objects.get(id=movie_session_id)
    except MovieSession.DoesNotExist:
        return None


def update_movie_session(
        session_id: int,
        show_time: Optional[str] = None,
        movie_id: Optional[int] = None,
        cinema_hall_id: Optional[int] = None
) -> Optional[MovieSession]:
    try:
        movie_session = MovieSession.objects.get(id=session_id)
    except MovieSession.DoesNotExist:
        return None

    if show_time is not None:
        movie_session.show_time = show_time

    if movie_id is not None:
        try:
            movie = Movie.objects.get(id=movie_id)
            movie_session.movie = movie
        except Movie.DoesNotExist:
            pass

    if cinema_hall_id is not None:
        try:
            cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
            movie_session.cinema_hall = cinema_hall
        except CinemaHall.DoesNotExist:
            pass

    movie_session.save()
    return movie_session


def delete_movie_session_by_id(session_id: int) -> None:
    try:
        movie_session = MovieSession.objects.get(id=session_id)
        movie_session.delete()
    except MovieSession.DoesNotExist:
        pass
