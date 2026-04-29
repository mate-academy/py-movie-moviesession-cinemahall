from datetime import datetime

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> MovieSession:
    new_movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )
    return new_movie_session


def get_movies_sessions(session_date: str = None) -> QuerySet:
    session_queryset = MovieSession.objects.all()
    if session_date:
        session_queryset = session_queryset.filter(
            show_time__date=session_date
        )
    return session_queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> MovieSession:
    session_queryset = MovieSession.objects.get(
        id=session_id
    )
    if show_time:
        session_queryset.show_time = (
            show_time
        )
    if cinema_hall_id:
        session_queryset.cinema_hall_id = cinema_hall_id
    if movie_id:
        session_queryset.movie_id = movie_id
    session_queryset.save()
    return session_queryset


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
