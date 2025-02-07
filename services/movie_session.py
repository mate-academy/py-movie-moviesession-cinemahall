import datetime
from django.db.models import QuerySet
from db.models import MovieSession


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int
                         ) -> MovieSession:
    return MovieSession.objects.create(
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id,
        show_time=movie_show_time
    )


def get_movie_sessions(session_date: datetime = None) -> QuerySet:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)

    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id:int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None
                         ) -> None:
    MovieSession.objects.update(
        session_id=session_id,
        show_time=show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def delete_movie_session(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
