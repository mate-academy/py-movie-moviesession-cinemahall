from datetime import datetime

from django.db.models import QuerySet

from db.models import MovieSession, CinemaHall, Movie


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> None:
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    movie = Movie.objects.get(id=movie_id)
    MovieSession.objects.create(show_time=movie_show_time,
                                cinema_hall=cinema_hall,
                                movie=movie)


def get_movies_sessions(session_date: str = None) -> QuerySet:
    if session_date:
        queryset = MovieSession.objects.filter(show_time__date=session_date)
    else:
        queryset = MovieSession.objects.all()
    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> None:
    if show_time:
        MovieSession.objects.filter(
            id=session_id).update(show_time=show_time)
    if movie_id:
        MovieSession.objects.filter(
            id=session_id).update(movie_id=movie_id)
    if cinema_hall_id:
        MovieSession.objects.filter(
            id=session_id).update(cinema_hall_id=cinema_hall_id)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
