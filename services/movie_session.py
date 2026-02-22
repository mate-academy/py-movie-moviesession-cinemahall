from db.models import MovieSession

from django.db.models import QuerySet

import datetime


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int,
                         ) -> MovieSession:
    new_session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id,
    )
    return new_session


def get_movies_sessions(session_date: str = None) -> QuerySet:
    queryset = MovieSession.objects.all()
    if session_date:
        date_obj = datetime.datetime.strptime(session_date,
                                              "%Y-%m-%d").date()
        queryset = queryset.filter(show_time__date=date_obj)
    return queryset


def get_movie_session_by_id(id_: int) -> MovieSession:
    return MovieSession.objects.get(id=id_)


def update_movie_session(session_id: int,
                         show_time: datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None,
                         ) -> MovieSession:
    updated_session = MovieSession.objects.get(id=session_id)
    if show_time:
        updated_session.show_time = show_time
    if movie_id:
        updated_session.movie_id = movie_id
    if cinema_hall_id:
        updated_session.cinema_hall_id = cinema_hall_id
    updated_session.save()
    return updated_session


def delete_movie_session_by_id(session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=session_id).delete()
