from datetime import date, datetime
from typing import Optional
from django.db.models import QuerySet
from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(
    movie_show_time: datetime, movie_id: int, cinema_hall_id: int
) -> MovieSession:
    """
    Creates a new movie session.

    Args:
        movie_show_time (datetime): The date and time of the movie session.
        movie_id (int): The ID of the movie for the session.
        cinema_hall_id (int): The ID of the cinema hall for the session.

    Returns:
        MovieSession: The newly created MovieSession object.
    """
    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    return MovieSession.objects.create(
        show_time=movie_show_time, movie=movie, cinema_hall=cinema_hall
    )


def get_movies_sessions(
    session_date: Optional[date] = None
) -> QuerySet[MovieSession]:
    """
    Retrieves movie sessions, optionally filtered by date.

    Args:
        session_date (Optional[date]): The date to filter sessions by.
                                       If None, all sessions are returned.

    Returns:
        QuerySet[MovieSession]: A queryset of MovieSession objects.
    """
    queryset = MovieSession.objects.all()
    if session_date:
        return queryset.filter(show_time__date=session_date)
    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    """
    Retrieves a single movie session by its ID.

    Args:
        movie_session_id (int): The ID of the movie session to retrieve.

    Returns:
        MovieSession: The MovieSession object.
    """
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
    session_id: int,
    show_time: Optional[datetime] = None,
    movie_id: Optional[int] = None,
    cinema_hall_id: Optional[int] = None,
) -> MovieSession:
    """
    Updates an existing movie session.

    Args:
        session_id (int): The ID of the movie session to update.
        show_time (Optional[datetime]): New show time for the session.
        movie_id (Optional[int]): New movie ID for the session.
        cinema_hall_id (Optional[int]): New cinema hall ID for the session.

    Returns:
        MovieSession: The updated MovieSession object.
    """
    session = MovieSession.objects.get(id=session_id)

    if show_time:
        session.show_time = show_time
    if movie_id:
        session.movie = Movie.objects.get(id=movie_id)
    if cinema_hall_id:
        session.cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)

    session.save()
    return session


def delete_movie_session_by_id(session_id: int) -> None:
    """
    Deletes a movie session by its ID.

    Args:
        session_id (int): The ID of the movie session to delete.
    """
    session = MovieSession.objects.get(id=session_id)
    session.delete()
