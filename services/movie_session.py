from django.db.models import QuerySet
import init_django_orm  # noqa: F401
import datetime
from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> QuerySet:
    new_movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )
    return new_movie_session


def get_movies_sessions(session_date: str = None) -> QuerySet:
    queryset = MovieSession.objects.all()
    if session_date is not None:
        queryset = queryset.filter(
            show_time__year=session_date.split("-")[0],
            show_time__month=session_date.split("-")[1],
            show_time__day=session_date.split("-")[2]
        )

    return queryset


def get_movie_session_by_id(movie_session_id: int) -> str:
    return MovieSession.objects.filter(id=movie_session_id).first()


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> QuerySet:
    queryset_session_for_update = MovieSession.objects.filter(
        id=session_id
    )

    if show_time is not None:
        queryset_session_for_update.update(
            show_time=show_time
        )
    if movie_id is not None:
        queryset_session_for_update.update(
            movie_id=movie_id
        )
    if cinema_hall_id is not None:
        queryset_session_for_update.update(
            cinema_hall_id=cinema_hall_id
        )

    return queryset_session_for_update


def delete_movie_session_by_id(session_id: int) -> None:
    movie_session = MovieSession.objects.filter(id=session_id).first()
    movie_session.delete()
