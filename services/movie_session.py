import datetime
from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime.datetime,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movies_sessions(
        session_date: str | None = None
) -> QuerySet[MovieSession]:
    sessions = MovieSession.objects.all()
    if session_date:
        date = datetime.datetime.strptime(session_date, "%Y-%m-%d")
        sessions = sessions.filter(
            show_time__date=date
        )
    return sessions


def get_movie_session_by_id(
        movie_session_id: int
) -> QuerySet[MovieSession]:
    return MovieSession.objects.get(
        id=movie_session_id
    )


def update_movie_session(
        session_id: int,
        show_time: str | None = None,
        movie_id: int | None = None,
        cinema_hall_id: int | None = None
) -> None:
    session = get_movie_session_by_id(session_id)
    if show_time:
        session.show_time = show_time
    if movie_id:
        session.movie_id = movie_id
    if cinema_hall_id:
        session.cinema_hall_id = cinema_hall_id
    session.save()


def delete_movie_session_by_id(
        session_id: int
) -> None:
    session = get_movie_session_by_id(session_id)
    session.delete()
