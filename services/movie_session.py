from datetime import datetime
from django.db.models import QuerySet
from db.models import MovieSession


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> MovieSession:
    session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )
    return session


def get_movies_sessions(session_date: str = None) -> QuerySet:
    sessions = MovieSession.objects.all()

    if session_date:
        query_date = datetime.strptime(session_date, "%Y-%m-%d").date()
        sessions = sessions.filter(show_time__date=query_date)

    return sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession | None:
    return MovieSession.objects.filter(id=movie_session_id).first()


def update_movie_session(
    session_id: int,
    show_time: datetime = None,
    movie_id: int = None,
    cinema_hall_id: int = None
) -> MovieSession | None:
    session = MovieSession.objects.filter(id=session_id).first()
    if not session:
        return None

    if show_time:
        session.show_time = show_time
    if movie_id:
        session.movie_id = movie_id
    if cinema_hall_id:
        session.cinema_hall_id = cinema_hall_id

    session.save()
    return session


def delete_movie_session_by_id(session_id: int) -> bool:
    deleted, _ = MovieSession.objects.filter(id=session_id).delete()
    return deleted > 0
