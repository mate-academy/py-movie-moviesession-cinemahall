from datetime import datetime

from django.db.models import QuerySet
from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie=movie, cinema_hall=cinema_hall
    )


def get_movies_sessions(movie_show_time: str = None) -> QuerySet:
    queryset = MovieSession.objects.all()

    if movie_show_time:
        queryset = queryset.filter(show_time__date=movie_show_time)

    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    queryset = MovieSession.objects.filter(id=session_id)

    if show_time:
        queryset.update(show_time=show_time)
    if movie_id:
        queryset.update(movie_id=movie_id)
    if cinema_hall_id:
        queryset.update(cinema_hall_id=cinema_hall_id)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
