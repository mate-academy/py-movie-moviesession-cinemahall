from datetime import datetime

from db.models import MovieSession
from django.db.models import QuerySet


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movies_sessions(
        session_date: str = None
) -> QuerySet:
    if session_date:
        return MovieSession.objects.all().filter(
            show_time__date=session_date
        )
    else:
        return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> str:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> QuerySet:
    sess = MovieSession.objects.all()

    if show_time is not None:
        sess.update(
            show_time=show_time
        )
    if movie_id is not None:
        sess.filter(id=session_id).update(
            movie=movie_id
        )
    if cinema_hall_id is not None:
        sess.update(
            cinema_hall=cinema_hall_id
        )
    return sess


def delete_movie_session_by_id(
        session_id: int
) -> MovieSession:
    return MovieSession.objects.filter(
        id=session_id
    ).delete()
