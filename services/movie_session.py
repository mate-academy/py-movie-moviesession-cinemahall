import logging
from datetime import datetime
from typing import Optional

from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from db.models import MovieSession

logger = logging.getLogger(__name__)


def create_movie_session(
    movie_show_time: datetime,
    movie_id: int,
    cinema_hall_id: int
) -> MovieSession:
    try:
        movie_session = MovieSession.objects.create(
            show_time=movie_show_time,
            movie_id=movie_id,
            cinema_hall_id=cinema_hall_id
        )
        return movie_session
    except Exception as e:
        logger.error(f"Error creating movie session: {e}")
        raise


def get_movies_sessions(session_date: Optional[str] = None) -> QuerySet:
    movies_sessions = MovieSession.objects.all()
    if session_date:
        movies_sessions = movies_sessions.filter(show_time__date=session_date)
    return movies_sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return get_object_or_404(MovieSession, pk=movie_session_id)


def update_movie_session(
    session_id: int,
    show_time: Optional[datetime] = None,
    movie_id: Optional[int] = None,
    cinema_hall_id: Optional[int] = None
) -> None:
    try:
        movie_session = MovieSession.objects.get(pk=session_id)

        if show_time:
            movie_session.show_time = show_time
        if movie_id is not None:
            movie_session.movie_id = movie_id
        if cinema_hall_id is not None:
            movie_session.cinema_hall_id = cinema_hall_id

        movie_session.save()
    except MovieSession.DoesNotExist:
        logger.error(f"Movie session with ID {session_id} does not exist.")
    except Exception as e:
        logger.error(f"Error updating movie session: {e}")


def delete_movie_session_by_id(session_id: int) -> None:
    try:
        movie_session = get_movie_session_by_id(session_id)
        if movie_session is not None:
            movie_session.delete()
    except MovieSession.DoesNotExist:
        logger.error(f"Movie session with ID {session_id} does not exist.")
    except Exception as e:
        logger.error(f"Error deleting movie session: {e}")
