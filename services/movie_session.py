from datetime import datetime

import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import MovieSession


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


def get_movies_sessions(session_date: str = None) -> QuerySet | str:
    try:
        if not session_date:
            return MovieSession.objects.all()
        date = datetime.strptime(session_date, "%Y-%m-%d").date()
        return MovieSession.objects.filter(
            show_time__date=date
        ).select_related(
            "movie"
        )
    except ValueError:
        return ("Incorrect date format."
                " Use the year-month-day format.")


def get_movie_session_by_id(movie_id: int) -> QuerySet:
    return MovieSession.objects.get(id=movie_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None,
) -> None:
    updates = {}
    if show_time:
        updates["show_time"] = show_time
    if movie_id:
        updates["movie_id"] = movie_id
    if cinema_hall_id:
        updates["cinema_hall_id"] = cinema_hall_id

    if updates:
        MovieSession.objects.filter(id=session_id).update(**updates)


def delete_movie_session_by_id(movie_session_id: int) -> None:
    MovieSession.objects.filter(id=movie_session_id).delete()
