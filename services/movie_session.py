from db.models import MovieSession
import datetime
from django.db.models import QuerySet


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int,
) -> QuerySet:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id,
    )


def get_movies_sessions(session_date: str = None) -> QuerySet:
    if session_date is not None:
        date_object = datetime.datetime.strptime(session_date, "%Y-%m-%d")
        return MovieSession.objects.filter(show_time__date=date_object)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_by_id: int) -> QuerySet:
    return MovieSession.objects.get(id=movie_session_by_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None,
) -> QuerySet:
    queryset = MovieSession.objects.all()
    if show_time is not None:
        queryset = MovieSession.objects.filter(
            id=session_id,
        ).update(show_time=show_time)
    if movie_id is not None:
        queryset = MovieSession.objects.filter(
            id=session_id,
        ).update(movie_id=movie_id)
    if cinema_hall_id is not None:
        queryset = MovieSession.objects.filter(
            id=session_id,
        ).update(cinema_hall_id=cinema_hall_id)
    return queryset


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
