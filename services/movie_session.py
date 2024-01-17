from django.db.models import QuerySet

from db.models import MovieSession

from db import models


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int) -> QuerySet[models.MovieSession]:

    new_movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id)
    return new_movie_session


def get_movies_sessions(
        session_date: str = None
) -> QuerySet[models.MovieSession]:

    queryset = MovieSession.objects.all()
    if session_date:
        queryset = queryset.filter(show_time__date=session_date)
    return queryset


def get_movie_session_by_id(
        movie_session_id: int
) -> QuerySet[models.MovieSession]:

    queryset = MovieSession.objects.get(pk=movie_session_id)
    return queryset


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None) -> QuerySet[models.MovieSession]:

    update_session = MovieSession.objects.get(pk=session_id)

    if show_time:
        update_session.show_time = show_time

    if movie_id:
        update_session.movie_id = movie_id

    if cinema_hall_id:
        update_session.cinema_hall_id = cinema_hall_id

    update_session.save()
    return update_session


def delete_movie_session_by_id(session_id: int) -> None:
    delete_session = MovieSession.objects.get(pk=session_id)
    delete_session.delete()
