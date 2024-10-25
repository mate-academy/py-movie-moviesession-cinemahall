from django.db.models import QuerySet
from datetime import datetime
from django.shortcuts import get_object_or_404

from db.models import MovieSession, CinemaHall, Movie


def create_movie_session(
    movie_show_time: datetime,
    movie_id: int,
    cinema_hall_id: int
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=get_object_or_404(CinemaHall, pk=cinema_hall_id),
        movie=get_object_or_404(Movie, pk=movie_id)
    )


def get_movies_sessions(session_time: str = None) -> QuerySet[MovieSession]:
    queryset = MovieSession.objects.all()
    if session_time:
        queryset = queryset.filter(show_time__date=session_time)
    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return get_object_or_404(MovieSession, pk=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    movie_session = get_movie_session_by_id(session_id)
    if show_time:
        movie_session.show_time = show_time
    if movie_id:
        movie_session.movie = (Movie.objects.get(pk=movie_id))
    if cinema_hall_id:
        movie_session.cinema_hall = (CinemaHall.objects.get(pk=cinema_hall_id))

    movie_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    get_movie_session_by_id(session_id).delete()
