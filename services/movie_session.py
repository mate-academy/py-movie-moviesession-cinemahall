from datetime import datetime, date

from typing import Union, List

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int,
) -> Union[MovieSession, QuerySet]:
    movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )

    return movie_session


def get_movies_sessions(session_date: str = None) -> QuerySet[MovieSession]:
    movie_sessions = MovieSession.objects.all()

    if session_date:
        session_date = datetime.strptime(session_date, '%Y-%m-%d').date()
        movie_sessions = movie_sessions.filter(show_time__date=session_date)

    return movie_sessions


def get_movie_session_by_id(movie_id: int) -> MovieSession:
    return MovieSession.objects.filter(movie_id=movie_id)


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> Union[MovieSession, QuerySet]:
    update_session = MovieSession.objects.filter(id=session_id)

    if show_time:
        update_session.update(show_time=show_time)

    if movie_id:
        update_session.update(movie_id=movie_id)

    if cinema_hall_id:
        update_session.update(cinema_hall_id=cinema_hall_id)

    return update_session


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
