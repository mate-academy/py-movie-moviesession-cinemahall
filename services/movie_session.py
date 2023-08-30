from datetime import datetime
from typing import Optional

from django.db.models import QuerySet

from db.models import CinemaHall, Movie, MovieSession


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(session_date: Optional[datetime] = None) -> QuerySet:
    searched_session = MovieSession.objects.all()

    if session_date:
        searched_session = searched_session.filter(
            show_time__date=session_date
        )

    return searched_session


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: Optional[datetime] = None,
        movie_id: Optional[int] = None,
        cinema_hall_id: Optional[int] = None
) -> None:
    update_session = MovieSession.objects.get(id=session_id)

    if show_time:
        update_session.show_time = show_time

    if movie_id:
        update_session.movie = Movie.objects.get(id=movie_id)

    if cinema_hall_id:
        update_session.cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)

    update_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
