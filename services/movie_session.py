import datetime

from db.models import MovieSession
from django.db.models.query import QuerySet


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


def get_movies_sessions(session_date: str = None) -> QuerySet:
    movies_sessions = MovieSession.objects.all()

    if session_date:
        return movies_sessions.filter(show_time__date=session_date)

    return movies_sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
    session_id: int,
    show_time: datetime = None,
    movie_id: int = None,
    cinema_hall_id: int = None
) -> int:
    movie_session = MovieSession.objects.get(id=session_id)
    changes = 0

    if show_time:
        movie_session.show_time = show_time
        changes += 1

    if movie_id:
        movie_session.movie_id = movie_id
        changes += 1

    if cinema_hall_id:
        movie_session.cinema_hall_id = cinema_hall_id
        changes += 1

    movie_session.save()

    return changes


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
