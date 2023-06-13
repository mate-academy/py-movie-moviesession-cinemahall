from datetime import datetime

from typing import Optional

from django.db.models import QuerySet

from db.models import Movie, CinemaHall, MovieSession


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=CinemaHall.objects.get(id=cinema_hall_id),
        movie=Movie.objects.get(id=movie_id),
    )


def get_movies_sessions(session_date: Optional[str] = None) -> QuerySet:
    new_sessions = MovieSession.objects.all()

    if session_date:
        session_date = datetime.strptime(session_date, "%Y-%m-%d")
        new_sessions = new_sessions.filter(show_time__date=session_date)

    return new_sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: Optional[str] = None,
        movie_id: Optional[int] = None,
        cinema_hall_id: Optional[int] = None
) -> None:
    session = MovieSession.objects.get(id=session_id)

    if show_time:
        session.show_time = show_time

    if movie_id:
        session.movie = Movie.objects.get(id=movie_id)

    if cinema_hall_id:
        session.cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)

    session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()