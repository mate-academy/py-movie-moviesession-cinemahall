from datetime import datetime
from typing import Optional, List

from db.models import CinemaHall, Movie, MovieSession


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id,
    )


def get_movies_sessions(session_date: datetime = None) -> List[MovieSession]:
    """
    Retrieve movie sessions, optionally filtered by a specific date.
    """
    # If a session date is provided, parse it and filter sessions
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)

    # If no session date is provided, return all movie sessions
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> Optional[MovieSession]:
    """
    Retrieve a movie session by its ID.
    """
    try:
        return MovieSession.objects.get(id=movie_session_id)
    except MovieSession.DoesNotExist:
        return None


def update_movie_session(session_id: int,
                         show_time: datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> Optional[MovieSession]:
    """
    Update a movie session's details by its ID.
    """
    try:
        # Retrieve the movie session
        movie_session = MovieSession.objects.get(id=session_id)

        # Update fields if new values are provided
        if show_time:
            movie_session.show_time = show_time
        if movie_id:
            movie_session.movie = Movie.objects.get(id=movie_id)
        if cinema_hall_id:
            movie_session.cinema_hall = CinemaHall.objects.get(
                id=cinema_hall_id
            )

        # Save changes
        movie_session.save()
        return movie_session
    except MovieSession.DoesNotExist:
        return None


def delete_movie_session_by_id(session_id: int) -> bool:
    """
    Delete a movie session by its ID.
    """
    try:
        movie_session = MovieSession.objects.get(id=session_id)
        movie_session.delete()
        return True
    except MovieSession.DoesNotExist:
        return False
