from datetime import datetime

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(movie_show_time: datetime, movie_id: int,
                         cinema_hall_id: int) -> None:
    MovieSession.objects.create(show_time=movie_show_time,
                                cinema_hall_id=cinema_hall_id,
                                movie_id=movie_id
                                )


def get_movies_sessions(session_date: datetime = None) -> QuerySet:
    queryset = MovieSession.objects.all()
    if session_date is not None:
        queryset = queryset.filter(show_time__date=session_date)

    return queryset


def get_movie_session_by_id(movie_session_id: int) -> QuerySet:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None
                         ) -> None:
    new_session = MovieSession.objects.get(id=session_id)

    if show_time is not None:
        new_session.show_time = show_time

    if movie_id is not None:
        new_session.movie_id = movie_id

    if cinema_hall_id is not None:
        new_session.cinema_hall_id = cinema_hall_id

    new_session.save()


def delete_movie_session_by_id(session_id: int) -> QuerySet:
    MovieSession.objects.filter(id=session_id).delete()
