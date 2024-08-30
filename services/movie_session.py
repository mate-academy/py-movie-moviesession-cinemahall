from datetime import datetime
from typing import Optional, Any

from django.core.exceptions import ObjectDoesNotExist

from db.models import MovieSession, CinemaHall, Movie


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int,
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id,
    )


def get_movies_sessions(session_date: str = "") -> MovieSession | None:
    sessions = MovieSession.objects.all()
    if session_date:
        sessions = sessions.filter(
            show_time__date=session_date
        )
    return sessions


def get_movie_session_by_id(movie_id: int) -> MovieSession:
    return MovieSession.objects.get(pk=movie_id)


def update_movie_session(
        session_id: int,
        show_time: Optional[datetime] = None,
        movie_id: Optional[int] = None,
        cinema_hall_id: Optional[int] = None
) -> tuple[Any, Any]:
    if not any([show_time, movie_id, cinema_hall_id]):
        return
    try:
        movie_session = MovieSession.objects.get(pk=session_id)
    except ObjectDoesNotExist:
        raise ObjectDoesNotExist(
            f"Movie Session with ID {session_id} does not exist"
        )
    else:
        if show_time:
            movie_session.show_time = show_time
        if cinema_hall_id:
            movie_session.cinema_hall = (
                CinemaHall.objects.get(pk=cinema_hall_id)
            )
        if movie_id:
            movie_session.movie = Movie.objects.get(pk=movie_id)
        movie_session.save()
        return movie_session.cinema_hall_id, movie_session.movie_id


def delete_movie_session_by_id(session_id: int) -> MovieSession:
    return MovieSession.objects.get(pk=session_id).delete()
