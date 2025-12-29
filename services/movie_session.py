import datetime

from django.db.models.query import QuerySet

from db.models import MovieSession


def create_movie_session(movie_show_time: datetime.datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> None:
    MovieSession.objects.create(show_time=movie_show_time,
                                movie_id=movie_id,
                                cinema_hall_id=cinema_hall_id)


def get_movies_sessions(session_date: datetime = None) -> QuerySet:
    movie_session = MovieSession.objects.all()

    if session_date:
        movie_session = MovieSession.objects.filter(
            show_time__date=session_date
        )
    return movie_session


def get_movie_session_by_id(movie_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_id)


def update_movie_session(session_id: int,
                         show_time: datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> None:
    try:
        MovieSession.objects.get(id=session_id)
    except MovieSession.DoesNotExist:
        return

    updates = {}

    if show_time:
        updates["show_time"] = show_time
    if cinema_hall_id:
        updates["cinema_hall_id"] = cinema_hall_id
    if movie_id:
        updates["movie_id"] = movie_id
    if updates:
        MovieSession.objects.filter(id=session_id).update(**updates)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
