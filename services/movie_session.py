from datetime import datetime
from typing import Optional
from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    """
    Creates a new movie session.

    :param movie_show_time: Movie show time
    :param movie_id: Movie ID
    :param cinema_hall_id: Cinema hall ID
    :return: Created MovieSession object
    """
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(
        session_date: Optional[str] = None
) -> QuerySet[MovieSession]:
    """
    Returns movie sessions, optionally filtered by date.

    :param session_date: Date in format "YYYY-MM-DD" (optional)
    :return: QuerySet of movie sessions
    """
    queryset = MovieSession.objects.all()

    if session_date is not None:
        date_obj = datetime.strptime(session_date, "%Y-%m-%d").date()
        queryset = queryset.filter(show_time__date=date_obj)

    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    """
    Returns a movie session by ID.

    :param movie_session_id: Movie session ID
    :return: MovieSession object
    """
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: Optional[datetime] = None,
        movie_id: Optional[int] = None,
        cinema_hall_id: Optional[int] = None
) -> MovieSession:
    """
    Updates a movie session with provided fields.

    :param session_id: Movie session ID
    :param show_time: New show time (optional)
    :param movie_id: New movie ID (optional)
    :param cinema_hall_id: New cinema hall ID (optional)
    :return: Updated MovieSession object
    """
    movie_session = MovieSession.objects.get(id=session_id)

    if show_time is not None:
        movie_session.show_time = show_time

    if movie_id is not None:
        movie_session.movie_id = movie_id

    if cinema_hall_id is not None:
        movie_session.cinema_hall_id = cinema_hall_id

    movie_session.save()
    return movie_session


def delete_movie_session_by_id(session_id: int) -> None:
    """
    Deletes a movie session by ID.

    :param session_id: Movie session ID
    """
    MovieSession.objects.filter(id=session_id).delete()
