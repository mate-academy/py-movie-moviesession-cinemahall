from django.db.models import QuerySet
from django.utils import timezone
from db.models import MovieSession
import datetime


def create_movie_session(
        movie_show_time: datetime.datetime,
        movie_id: int,
        cinema_hall_id: int,
) -> MovieSession:
    if timezone.is_naive(movie_show_time):
        movie_show_time = timezone.make_aware(movie_show_time)
    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id,
    )


def get_movies_sessions(
        session_date: str | None = None,
) -> QuerySet:
    if session_date:
        return MovieSession.objects.filter(
            show_time__date=session_date
        )
    return MovieSession.objects.all()


def get_movie_session_by_id(
        movie_session_id: int,
) -> MovieSession:
    return MovieSession.objects.get(
        id=movie_session_id
    )


def update_movie_session(
        session_id: int,
        show_time: datetime.datetime | None = None,
        movie_id: int | None = None,
        cinema_hall_id: int | None = None,
) -> None:
    update_data = {}
    if show_time is not None:
        if timezone.is_naive(show_time):
            show_time = timezone.make_aware(show_time)
        update_data["show_time"] = show_time
    if cinema_hall_id is not None:
        update_data["cinema_hall_id"] = cinema_hall_id
    if movie_id is not None:
        update_data["movie_id"] = movie_id
    if update_data:
        MovieSession.objects.filter(
            id=session_id
        ).update(**update_data)


def delete_movie_session_by_id(
        session_id: int,
) -> None:
    MovieSession.objects.filter(
        id=session_id
    ).delete()
