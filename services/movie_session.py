from django.db.models import QuerySet

from db.models import MovieSession
from datetime import datetime


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    movie_session_create = MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )
    return movie_session_create


def get_movies_sessions(session_date: datetime = None) -> QuerySet:
    queryset = MovieSession.objects.all()
    if session_date:

        session_date = datetime.datetime.strptime(
            session_date, "%Y-%m-%d"
        ).date()

        queryset = queryset.filter(data=session_date)

    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    movie_session = MovieSession.objects.get(id=movie_session_id)
    return movie_session


def update_movie_session(
    session_id: int,
    show_time: datetime = None,
    movie_id: int = None,
    cinema_hall_id: int = None
) -> None:
    movie_session = MovieSession.objects.get(id=session_id)

    if show_time is not None:
        movie_session.show_time = show_time
    if movie_id is not None:
        movie_session.movie_id = movie_id
    if cinema_hall_id is not None:
        movie_session.cinema_hall_id = cinema_hall_id

    movie_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
