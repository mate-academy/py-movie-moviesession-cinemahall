from db.models import MovieSession
from datetime import datetime
from typing import Optional, List


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id,
    )


def get_movies_sessions(session_date: datetime = None) -> MovieSession:
    sessions = MovieSession.objects.all()
    if session_date:
        sessions = sessions.filter(show_time__date=session_date)
    return sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: Optional[List[int]] = None,
        cinema_hall_id: Optional[List[int]] = None
) -> MovieSession:
    updated_fields = {}
    if show_time is not None:
        updated_fields["show_time"] = show_time
    if movie_id is not None:
        updated_fields["movie"] = movie_id
    if cinema_hall_id is not None:
        updated_fields["cinema_hall"] = cinema_hall_id

    session = MovieSession.objects.filter(
        id=session_id
    ).update(**updated_fields)
    return session


def delete_movie_session_by_id(session_id: int) -> None:
    movie_session = MovieSession.objects.get(id=session_id)
    movie_session.delete()
