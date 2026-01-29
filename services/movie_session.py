import datetime
from typing import Optional

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
    movie_show_time: datetime.datetime,
    movie_id: int,
    cinema_hall_id: int,
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id,
    )


def get_movies_sessions(date: Optional[str] = None) -> QuerySet[MovieSession]:
    queryset = MovieSession.objects.select_related(
        "movie",
        "cinema_hall",
    ).all()

    if date:
        year, month, day = (int(value) for value in date.split("-"))
        queryset = queryset.filter(
            show_time__date=datetime.date(year, month, day)
        )

    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.select_related(
        "movie",
        "cinema_hall",
    ).get(id=movie_session_id)


def update_movie_session(
    session_id: int,
    show_time: Optional[datetime.datetime] = None,
    movie_id: Optional[int] = None,
    cinema_hall_id: Optional[int] = None,
) -> MovieSession:
    session = MovieSession.objects.get(id=session_id)

    if show_time is not None:
        session.show_time = show_time

    if movie_id is not None:
        session.movie_id = movie_id

    if cinema_hall_id is not None:
        session.cinema_hall_id = cinema_hall_id

    session.save()
    return session


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
