from db.models import MovieSession
from datetime import datetime
from django.db.models.query import QuerySet


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(session_date: str = None) -> QuerySet:
    queryset = MovieSession.objects.all()

    if session_date is not None:
        ses = datetime.strptime(session_date, "%Y-%m-%d")
        queryset = queryset.filter(show_time__date=ses)

    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> QuerySet:
    movie_session = MovieSession.objects.filter(id=session_id)

    to_update = {}

    if show_time is not None:
        to_update["show_time"] = show_time

    if movie_id is not None:
        to_update["movie_id"] = movie_id

    if cinema_hall_id is not None:
        to_update["cinema_hall_id"] = cinema_hall_id

    movie_session.update(**to_update)

    return movie_session


def delete_movie_session_by_id(session_id: int) -> None:
    return get_movie_session_by_id(session_id).delete()
