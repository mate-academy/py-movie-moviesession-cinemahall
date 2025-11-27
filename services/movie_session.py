import datetime
from typing import Optional
from django.db.models import QuerySet
from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime.datetime,
        movie_id: int,
        cinema_hall_id: int) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id,
    )


def get_movies_sessions(session_date: Optional[str] = None) -> QuerySet:
    if session_date:
        correct_date = datetime.datetime.strptime(session_date, "%Y-%m-%d")
        return MovieSession.objects.filter(
            show_time__date=correct_date.date()
        )
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: Optional[datetime.datetime] = None,
        movie_id: Optional[int] = None,
        cinema_hall_id: Optional[int] = None) -> None:

    exact_session = MovieSession.objects.get(id=session_id)
    if show_time is not None:
        exact_session.show_time = show_time
    if movie_id is not None:
        exact_session.movie_id = movie_id
    if cinema_hall_id is not None:
        exact_session.cinema_hall_id = cinema_hall_id
    exact_session.save()


def delete_movie_session_by_id(movie_session_id: int) -> None:
    MovieSession.objects.get(id=movie_session_id).delete()
