from datetime import datetime
from typing import Optional
from django.db.models import QuerySet
from db.models import MovieSession


def create_movie_session(
        movie_show_time: int,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )
    return movie_session


def get_movies_sessions(
        session_date: Optional[str] = None,
) -> QuerySet[MovieSession]:
    session = MovieSession.objects.all()
    if session_date is not None:
        date_info = datetime.strptime(session_date, "%Y-%m-%d").date()
        session = MovieSession.objects.filter(show_time__date=date_info)
    return session


def get_movie_session_by_id(
        movie_session_id: int
) -> "MovieSession":
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: Optional[int] = None,
        movie_id: Optional[int] = None,
        cinema_hall_id: Optional[int] = None,
) -> None:

    session = MovieSession.objects.get(id=session_id)

    if show_time:
        session.show_time = show_time

    if movie_id:
        session.movie_id = movie_id

    if cinema_hall_id:
        session.cinema_hall_id = cinema_hall_id

    session.save()


def delete_movie_session_by_id(
        session_id: int
) -> None:
    session = get_movie_session_by_id(session_id)
    session.delete()
