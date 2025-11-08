from datetime import datetime

from django.db.models import QuerySet

from db.models import MovieSession
from django.utils import timezone


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> None:

    naive_datetime = datetime.strptime(movie_show_time, "%Y-%m-%d %H:%M:%S")
    aware_datetime = timezone.make_aware(naive_datetime)

    MovieSession.objects.create(
        show_time=aware_datetime,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    movie_session_obj = MovieSession.objects.get(id=movie_session_id)
    return movie_session_obj


def get_movies_sessions(
        session_date: str | None = None
) -> QuerySet[MovieSession]:
    queryset = MovieSession.objects.all()
    if session_date:
        queryset = queryset.filter(show_time__date=session_date)
    return queryset


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    movie_session_obj = MovieSession.objects.get(id=session_id)



    if show_time is not None:
        naive_datetime = datetime.strptime(show_time, "%Y-%m-%d %H:%M:%S")
        aware_datetime = timezone.make_aware(naive_datetime)
        movie_session_obj.show_time = aware_datetime
        movie_session_obj.save()
    if movie_id is not None:
        movie_session_obj.movie_id = movie_id
        movie_session_obj.save()
    if cinema_hall_id is not None:
        movie_session_obj.cinema_hall_id = cinema_hall_id
        movie_session_obj.save()


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
