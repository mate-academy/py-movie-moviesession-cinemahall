from django.utils import timezone
from django.db.models import QuerySet
from datetime import datetime

from db.models import MovieSession


def create_movie_session(
        movie_show_time: timezone.datetime,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    if timezone.is_naive(movie_show_time):
        movie_show_time = timezone.make_aware(
            movie_show_time,
            timezone.get_current_timezone()
        )

    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movies_sessions(session_date: str = None) -> QuerySet:
    if session_date:
        session_date = datetime.strptime(session_date, "%Y-%m-%d")
        return MovieSession.objects.filter(
            show_time__date=session_date
        )
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: timezone.datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    if show_time:
        if timezone.is_naive(show_time):
            show_time = timezone.make_aware(
                show_time,
                timezone.get_current_timezone()
            )

    update_data = {}
    if show_time:
        update_data["show_time"] = show_time
    if movie_id:
        update_data["movie_id"] = movie_id
    if cinema_hall_id:
        update_data["cinema_hall_id"] = cinema_hall_id
    MovieSession.objects.filter(id=session_id).update(**update_data)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
