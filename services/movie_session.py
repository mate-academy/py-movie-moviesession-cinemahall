from datetime import datetime

from django.db.models import QuerySet

import init_django_orm  # noqa:F401

from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(
        session_date: datetime = None
) -> QuerySet[MovieSession]:
    movies_sessions_in_current_date = MovieSession.objects.all()
    if session_date is not None:
        movies_sessions_in_current_date = MovieSession.objects.filter(
            show_time__date=session_date)

    return movies_sessions_in_current_date


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    update_session = MovieSession.objects.filter(id=session_id)
    if show_time:
        update_session.update(show_time=show_time)

    if movie_id:
        update_session.update(movie_id=movie_id)

    if cinema_hall_id:
        update_session.update(cinema_hall_id=cinema_hall_id)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
