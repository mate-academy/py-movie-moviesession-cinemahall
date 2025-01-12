import init_django_orm  # noqa: F401
from datetime import datetime
from typing import List, Optional
from db.models import MovieSession


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> "MovieSession":
    return MovieSession.objects.create(
        show_time=datetime.strptime(
            movie_show_time,
            "%Y-%m-%d %H:%M:%S"
        ),
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )

def get_movie_sessions(session_date: Optional[str]) -> "List[MovieSession]":
    if session_date:
        date_filter = datetime.strptime(session_date, "%Y-%m-%d").date()
        return list(MovieSession.objects.filter(show_time__date=date_filter))
    return list(MovieSession.objects.all())

def get_movie_session_by_id(movie_session_id: int) -> Optional["MovieSession"]:
    try:
        return MovieSession.objects.get(id=movie_session_id)
    except MovieSession.DoesNotExist:
        return None

def update_movie_session(
        movie_session_id: int,
        show_time: Optional[str] = None,
        movie_id: Optional[int] = None,
        cinema_hall_id: Optional[int] = None,
) -> Optional["MovieSession"]:
    try:
        session = MovieSession.objects.get(id=movie_session_id)
        if show_time:
            session.show_time = datetime.strptime(
                show_time,
                "%Y-%m-%d %H:%M:%S")
        if movie_id:
            session.movie_id = movie_id
        if cinema_hall_id:
            session.cinema_hall_id = cinema_hall_id
        session.save()
        return session
    except MovieSession.DoesNotExist:
        return None

def delete_movie_session_by_id(session_id: int) -> bool:
    try:
        session = MovieSession.objects.get(id=session_id)
        session.delete()
        return True
    except MovieSession.DoesNotExist:
        return False
