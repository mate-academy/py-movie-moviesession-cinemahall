import datetime

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> QuerySet:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id,
    )


def get_movies_sessions(session_date: datetime = None) -> QuerySet:
    if session_date is not None:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> QuerySet:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        cinema_hall_id: int = None,
        show_time: datetime = None,
        movie_id: int = None
) -> None:
    if movie_id:
        MovieSession.objects.filter(
            id=session_id
        ).update(movie=movie_id)
    if show_time:
        MovieSession.objects.filter(
            id=session_id
        ).update(show_time=show_time)
    if cinema_hall_id:
        MovieSession.objects.filter(
            id=session_id
        ).update(cinema_hall=cinema_hall_id)


def delete_movie_session_by_id(session_id: int) -> QuerySet:
    return MovieSession.objects.get(id=session_id).delete()
