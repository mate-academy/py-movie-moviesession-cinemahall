# flake8: noqa: E402
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()


from db.models import MovieSession, Movie, CinemaHall
from datetime import datetime
from django.db.models.query import QuerySet


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int,
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movies_sessions(sessions_date: str = None) -> QuerySet:
    movie_sessions = MovieSession.objects.all()
    if sessions_date:
        return movie_sessions.filter(
            show_time__date=datetime.strptime(sessions_date, "%Y-%m-%d")
        )
    return movie_sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(
        id=movie_session_id
    )


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    updated_session = MovieSession.objects.get(
        id=session_id
    )

    if show_time:
        updated_session.show_time = show_time

    if movie_id:
        updated_session.movie_id = movie_id

    if cinema_hall_id:
        updated_session.cinema_hall_id = cinema_hall_id

    updated_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(
        id=session_id
    ).delete()
