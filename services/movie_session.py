# movie_session.py

from typing import Optional, Union
from datetime import datetime
from db.models import MovieSession, Movie, CinemaHall
from django.db.models import QuerySet
from django.core.exceptions import ObjectDoesNotExist


def create_movie_session(movie_show_time: datetime, movie_id: int, cinema_hall_id: int) -> MovieSession:
    """
    Create a movie session with the provided parameters.

    :param movie_show_time: Show time of the movie
    :param movie_id: ID of the movie
    :param cinema_hall_id: ID of the cinema hall
    :return: Created MovieSession object
    """
    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)

    movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie=movie,
        cinema_hall=cinema_hall
    )

    return movie_session


def get_movies_sessions(session_date: Optional[str] = None) -> QuerySet:
    """
    Retrieve movie sessions based on an optional date.

    :param session_date: Optional date string in the format "year-month-day"
    :return: QuerySet of filtered movie sessions
    """
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)

    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> Optional[MovieSession]:
    """
    Retrieve a movie session by its ID.

    :param movie_session_id: ID of the movie session
    :return: MovieSession object or None if not found
    """
    try:
        return MovieSession.objects.get(id=movie_session_id)
    except ObjectDoesNotExist:
        return None


def update_movie_session(session_id: int,
                         show_time: Optional[datetime] = None,
                         movie_id: Optional[int] = None,
                         cinema_hall_id: Optional[int] = None) -> Optional[MovieSession]:
    """
    Update a movie session with the provided parameters if appropriate values are provided.

    :param session_id: ID of the movie session to update
    :param show_time: Optional new show time of the movie
    :param movie_id: Optional new ID of the movie
    :param cinema_hall_id: Optional new ID of the cinema hall
    :return: Updated MovieSession object or None if not found
    """
    try:
        movie_session = MovieSession.objects.get(id=session_id)

        if show_time:
            movie_session.show_time = show_time

        if movie_id:
            movie_session.movie = Movie.objects.get(id=movie_id)

        if cinema_hall_id:
            movie_session.cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)

        movie_session.save()  # Save the updated fields
        return movie_session

    except ObjectDoesNotExist:
        return None


def delete_movie_session_by_id(session_id: int) -> bool:
    """
    Delete a movie session with the provided ID.

    :param session_id: ID of the movie session to delete
    :return: True if deletion was successful, False if not found
    """
    try:
        movie_session = MovieSession.objects.get(id=session_id)
        movie_session.delete()
        return True
    except ObjectDoesNotExist:
        return False
