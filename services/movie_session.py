from db.models import MovieSession
from datetime import datetime
from django.db.models import QuerySet


def create_movie_session(
        movie_show_time: datetime | None = None,
        movie_id: int | None = None,
        cinema_hall_id: int = None
) -> MovieSession:
    new_movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id,
    )
    return new_movie_session


def get_movies_sessions(
        session_date: datetime | str = None
) -> QuerySet | MovieSession:
    if session_date:
        return MovieSession.objects.filter(
            show_time__date=session_date)
    else:
        return MovieSession.objects.all()


def get_movie_session_by_id(
        movie_session_id: int | None = None
) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int | None = None,
        show_time: datetime | None = None,
        movie_id: int | None = None,
        cinema_hall_id: int | None = None
) -> MovieSession:

    session = MovieSession.objects.get(id=session_id)
    if show_time:
        session.show_time = show_time
    if movie_id:
        session.movie_id = movie_id
    if cinema_hall_id:
        session.cinema_hall_id = cinema_hall_id
    session.save()
    return session


def delete_movie_session_by_id(
        session_id: int | None = None
) -> None:
    MovieSession.objects.get(id=session_id).delete()
