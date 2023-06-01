from datetime import datetime, timedelta

from django.db.models import QuerySet

from db.models import MovieSession
from services.cinema_hall import get_cinema_halls
from services.movie import get_movie_by_id


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int,

) -> None:
    cinema_hall = get_cinema_halls().get(pk=cinema_hall_id)
    movie = get_movie_by_id(movie_id)
    MovieSession.objects.create(
        show_time=movie_show_time,
        movie=movie,
        cinema_hall=cinema_hall
    )


def get_movies_sessions(
        session_date: str = None
) -> QuerySet:
    queryset = MovieSession.objects.all()
    if session_date:
        start_datetime = datetime.strptime(session_date, "%Y-%m-%d")
        end_datetime = start_datetime + timedelta(days=1)
        queryset = queryset.filter(
            show_time__range=[start_datetime, end_datetime]
        )
    return queryset


def get_movie_session_by_id(
        movie_session_id: int
) -> MovieSession:
    return MovieSession.objects.get(
        pk=movie_session_id
    )


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> MovieSession:
    movie_session = MovieSession.objects.get(pk=session_id)
    if movie_id:
        movie_session.movie_id = movie_id
    if cinema_hall_id:
        movie_session.cinema_hall_id = cinema_hall_id
    if show_time:
        movie_session.show_time = show_time
    movie_session.save()
    return movie_session


def delete_movie_session_by_id(session_id: int) -> None:
    get_movie_session_by_id(session_id).delete()
