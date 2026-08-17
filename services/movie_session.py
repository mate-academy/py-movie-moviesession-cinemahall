from typing import Optional
from datetime import datetime
from db.models import MovieSession
from django.db.models import QuerySet


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
        session_date: str | None = None
) -> QuerySet:
    if session_date:
        return MovieSession.objects.filter(
            show_time__date=session_date
        )
    return MovieSession.objects.all()


def get_movie_session_by_id(
        movie_session_id: int
) -> MovieSession:
    return MovieSession.objects.get(pk=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: Optional[datetime] = None,
        movie_id: Optional[int] = None,
        cinema_hall_id: Optional[int] = None
) -> MovieSession:
    fields_to_update = {
        "show_time": show_time,
        "cinema_hall_id": cinema_hall_id,
        "movie_id": movie_id
    }

    movie_session = MovieSession.objects.get(
        pk=session_id
    )

    for key, value in fields_to_update.items():
        if value is not None:
            setattr(movie_session, key, value)
    movie_session.save()

    return movie_session


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(pk=session_id).delete()
