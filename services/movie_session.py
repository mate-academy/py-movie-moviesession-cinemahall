from _datetime import datetime
from django.db.models import QuerySet
from typing import Optional

from db.models import MovieSession, CinemaHall, Movie


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    movie_session = MovieSession(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )
    movie_session.save()
    return movie_session


def get_movies_sessions(session_date: Optional[str] = None) -> QuerySet:
    sessions = MovieSession.objects.all()

    if session_date:
        date_session = datetime.strptime(session_date, "%Y-%m-%d").date()
        sessions = sessions.filter(show_time__date=date_session)

    return sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: Optional[datetime] = None,
        movie_id: Optional[int] = None,
        cinema_hall_id: Optional[int] = None
) -> None:
    session = MovieSession.objects.get(id=session_id)

    if show_time:
        session.show_time = show_time
    if movie_id:
        session.movie = Movie.objects.get(id=movie_id)
    if cinema_hall_id:
        session.cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)

    session.save()


def delete_movie_session_by_id(session_id: int) -> MovieSession:
    return MovieSession.objects.filter(id=session_id).delete()
