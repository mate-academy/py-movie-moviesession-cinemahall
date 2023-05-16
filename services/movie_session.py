from datetime import datetime
from db.models import MovieSession
from typing import Optional


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    movie_session = MovieSession(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )
    movie_session.save()
    return movie_session


def get_movies_sessions(
        session_date: Optional[str] = None
) -> Optional[MovieSession]:
    queryset = MovieSession.objects.all()

    if session_date:
        queryset = queryset.filter(show_time__date=session_date)

    return queryset


def get_movie_session_by_id(session_id: int) -> Optional[MovieSession]:
    try:
        return MovieSession.objects.get(id=session_id)
    except MovieSession.DoesNotExist:
        return None


def update_movie_session(
        session_id: int,
        show_time: Optional[datetime] = None,
        movie_id: Optional[int] = None,
        cinema_hall_id: Optional[int] = None
) -> Optional[MovieSession]:
    try:
        movie_session = MovieSession.objects.get(id=session_id)
        if show_time:
            movie_session.show_time = show_time
        if movie_id:
            movie_session.movie_id = movie_id
        if cinema_hall_id:
            movie_session.cinema_hall_id = cinema_hall_id
        movie_session.save()
        return movie_session
    except MovieSession.DoesNotExist:
        return None


def delete_movie_session_by_id(session_id: int) -> bool:
    try:
        movie_session = MovieSession.objects.get(id=session_id)
        movie_session.delete()
        return True
    except MovieSession.DoesNotExist:
        return False
