from django.db.models import QuerySet
from datetime import datetime

from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> None:

    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movies_sessions(
        session_date: str = None,

) -> QuerySet:

    query_set = MovieSession.objects.all()
    if session_date:
        query_set = query_set.filter(show_time__date=session_date)

    return query_set


def get_movie_session_by_id(
        movie_session_id: int
) -> MovieSession:

    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None,
) -> None:

    current_session = MovieSession.objects.get(id=session_id)

    if show_time:
        current_session.show_time = show_time
    if movie_id:
        current_session.movie_id = movie_id
    if cinema_hall_id:
        current_session.cinema_hall_id = cinema_hall_id

    current_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    session = MovieSession.objects.get(id=session_id)
    session.delete()
