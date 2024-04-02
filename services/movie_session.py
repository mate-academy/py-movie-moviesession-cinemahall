from datetime import datetime
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404

from db.models import Movie, CinemaHall, MovieSession
from services.movie import get_movie_by_id
from services.cinema_hall import get_cinema_hall_by_id


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> MovieSession:
    movie = get_object_or_404(Movie, pk=movie_id)
    cinema_hall = get_object_or_404(CinemaHall, pk=cinema_hall_id)
    return MovieSession.objects.create(show_time=movie_show_time,
                                       movie=movie,
                                       cinema_hall=cinema_hall)


def get_movies_sessions(session_date: datetime = None) -> QuerySet:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    else:
        return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> None | MovieSession:
    try:
        return MovieSession.objects.get(id=movie_session_id)
    except MovieSession.DoesNotExist:
        print(f"There is no such session id: {movie_session_id}")
        return None


def update_movie_session(session_id: int,
                         show_time: datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> None | MovieSession:
    session = get_movie_session_by_id(session_id)
    if not session:
        return None
    if show_time:
        session.show_time = show_time
    if movie_id:
        session.movie = get_movie_by_id(movie_id)
    if cinema_hall_id:
        session.cinema_hall = get_cinema_hall_by_id(cinema_hall_id)
    session.save()
    return session


def delete_movie_session_by_id(session_id: int) -> None:
    get_object_or_404(MovieSession, pk=session_id).delete()
