from datetime import datetime

from django.db.models import QuerySet
from django.http import QueryDict

from db.models import Movie, CinemaHall, MovieSession
from django.utils import timezone


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    movie_obj = Movie.objects.get(id=movie_id)
    cinema_obj = CinemaHall.objects.get(id=cinema_hall_id)

    naive_datetime = datetime.strptime(movie_show_time, '%Y-%m-%d %H:%M:%S')
    aware_datetime = timezone.make_aware(naive_datetime)

    if movie_obj and cinema_obj:
        MovieSession.objects.create(
            show_time=aware_datetime,
            cinema_hall_id=cinema_obj.id,
            movie_id=movie_obj.id
        )

def get_movie_session_by_id(movie_session_id) -> MovieSession:
    movie_session_obj = MovieSession.objects.get(id=movie_session_id)
    return movie_session_obj

def get_movie_sessions(session_date: str | None = None) -> QuerySet[MovieSession]:
    queryset = MovieSession.objects.all()
    if session_date:
        queryset = queryset.filter(show_time__date = session_date)
    return queryset

def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    movie_session_obj = MovieSession.objects.filter(id=session_id)

    update_data = {}

    if show_time is not None:
        update_data["show_time"] = show_time

    if movie_id is not None:
        update_data["movie_id"] = movie_id

    if cinema_hall_id is not None:
        update_data["cinema_hall_id"] = cinema_hall_id

    if update_data:
        movie_session_obj.update(**update_data)

def delete_movie_session(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
