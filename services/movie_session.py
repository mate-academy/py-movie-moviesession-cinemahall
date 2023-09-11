from django.db.models import QuerySet
from db.models import MovieSession
from datetime import datetime


def create_movie_session(
    movie_show_time: datetime, movie_id: int, cinema_hall_id: int
) -> MovieSession:
    movie_session: MovieSession = MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id,
    )
    return movie_session


def get_movies_sessions(
    session_date: str | None = None,
) -> QuerySet[MovieSession]:
    sessions: QuerySet = MovieSession.objects.all()
    if session_date is not None:
        date: datetime = datetime.strptime(session_date, "%Y-%m-%d")
        sessions = sessions.filter(show_time__date=date)
    return sessions


def get_movie_session_by_id(session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=session_id)


def update_movie_session(
    session_id: int,
    show_time: datetime | None = None,
    movie_id: int | None = None,
    cinema_hall_id: int | None = None,
) -> None:
    sessions: QuerySet = MovieSession.objects.filter(id=session_id)

    if show_time is not None:
        sessions.update(show_time=show_time)

    if movie_id is not None:
        sessions.update(movie_id=movie_id)

    if cinema_hall_id is not None:
        sessions.update(cinema_hall_id=cinema_hall_id)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
