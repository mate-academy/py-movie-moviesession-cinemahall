from django.db.models import QuerySet

from db.models import MovieSession

from datetime import datetime


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int,
) -> MovieSession:
    movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )
    return movie_session


def get_movies_sessions(
        session_date: datetime = None
) -> QuerySet | MovieSession:

    session = MovieSession.objects.all()

    if session_date:
        return session.filter(show_time__date=session_date)

    return session


def get_movie_session_by_id(
        movies_session_id: int,
) -> MovieSession:
    return MovieSession.objects.get(id=movies_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> QuerySet[MovieSession]:
    session = MovieSession.objects.filter(id=session_id)

    if show_time:
        session.update(show_time=show_time)

    if movie_id:
        session.update(movie_id=movie_id)

    if cinema_hall_id:
        session.update(cinema_hall_id=cinema_hall_id)

    return session


def delete_movie_session_by_id(session_id: int) -> tuple[int, dict[str, int]]:
    return MovieSession.objects.filter(id=session_id).delete()
