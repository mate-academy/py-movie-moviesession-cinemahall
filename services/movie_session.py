from django.db import models

from db.models import MovieSession


def create_movie_session(
        movie_show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(session_date: str = None) -> MovieSession:
    queryset = MovieSession.objects.all()
    if session_date:
        queryset = queryset.filter(show_time__date=session_date)
    return queryset


def get_movie_session_by_id(movie_id: int) -> models.Model:
    return MovieSession.objects.get(pk=movie_id)


def update_movie_session(
        session_id: int = None,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> MovieSession:
    session = MovieSession.objects.get(pk=session_id)

    if show_time:
        session.show_time = show_time

    if movie_id:
        session.movie_id = movie_id

    if cinema_hall_id:
        session.cinema_hall_id = cinema_hall_id

    session.save()
    return session


def delete_movie_session_by_id(movie_id: int):
    return MovieSession.objects.get(pk=movie_id).delete()
