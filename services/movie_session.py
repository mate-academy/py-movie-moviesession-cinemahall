from typing import List, Optional
import datetime

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(movie_show_time: datetime.date,
                         movie_id: int, cinema_hall_id: int) -> MovieSession:
    movie_session = MovieSession(
        movie_id=movie_id,
        cinema_hall=cinema_hall_id,
        show_time=movie_show_time
    )
    return movie_session


def get_movies_sessions(session_date: datetime.date
                        = None) -> List[MovieSession] | QuerySet:
    queryset = MovieSession.objects.all()
    if session_date is not None:
        queryset = queryset.filter(session_date=session_date)
    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession | QuerySet:
    queryset = MovieSession.objects.filter(movie_session_id=movie_session_id)
    return queryset


def update_movie_session(session_id: int,
                         show_time: Optional[str] = None,
                         movie_id: Optional[int] = None,
                         cinema_hall_id: Optional[int] = None) -> MovieSession:
    try:
        movie_session = MovieSession.objects.get(id=session_id)

        if show_time is not None:
            movie_session.show_time = show_time
        if movie_id is not None:
            movie_session.movie_id = movie_id
        if cinema_hall_id is not None:
            movie_session.cinema_hall_id = cinema_hall_id

        movie_session.save()
        return movie_session

    except MovieSession.DoesNotExist:
        raise ValueError(f"MovieSession with ID {session_id} does not exist.")


def delete_movie_session_by_id(movie_session_id: int) -> None:
    movie_session = MovieSession.objects.get(id=movie_session_id)
    movie_session.delete()
