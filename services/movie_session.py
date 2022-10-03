import init_django_orm  # noqa: F401

from db.models import Movie, MovieSession, CinemaHall

import datetime


def create_movie_session(movie_show_time: datetime, movie_id: int, cinema_hall_id: int):
    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=CinemaHall.objects.get(id=cinema_hall_id),
        movie=Movie.objects.get(id=movie_id)
    )


def get_movies_sessions(session_date=None):
    if session_date is None:
        return MovieSession.objects.all()
    dt = datetime.datetime.strptime(session_date, "%Y-%m-%d")
    return MovieSession.objects.filter(show_time__date=dt)


def get_movie_session_by_id(movie_session_id: int):
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time=None, movie_id=None, cinema_hall_id=None):
    queryset = MovieSession.objects.filter(id=session_id)
    if show_time is not None:
        queryset.update(show_time=show_time)
    if cinema_hall_id is not None:
        queryset.update(cinema_hall=CinemaHall.objects.get(id=cinema_hall_id))
    if movie_id is not None:
        queryset.update(movie=Movie.objects.get(id=movie_id))
    return MovieSession.objects.filter(id=session_id)


def delete_movie_session_by_id(session_id: int):
    return MovieSession.objects.filter(id=session_id).delete()
