# movie_session.py

from django.db.models import QuerySet
from db.models import MovieSession, CinemaHall, Movie
import datetime


def create_movie_session(
    movie_show_time: str | datetime.datetime,
    movie_id: int,
    cinema_hall_id: int
) -> MovieSession:
    """_summary_
    create_movie_session, takes movie_show_time - show time of the movie,
    movie_id - id of the movie, cinema_hall_id - id of the cinema hall.
    Creates movie session with provided parameters

    Args:
        movie_show_time (str | datetime.datetime): _description_
        movie_id (int): _description_
        cinema_hall_id (int): _description_

    Returns:
        MovieSession: _description_
    """
    if isinstance(movie_show_time, str):
        movie_show_time = datetime.datetime.strptime(
            movie_show_time, "%Y-%m-%d %H:%M:%S"
        )

    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie=Movie.objects.get(id=movie_id),
        cinema_hall=CinemaHall.objects.get(id=cinema_hall_id)
    )


def get_movies_sessions(
    session_date: str = None
) -> QuerySet:
    """_summary_
    get_movies_sessions, takes optional string session_date in such form:
    "year-month-day"
    -   if session_date is provided - returns all movie sessions for this date
    -   else returns all movies sessions

    Args:
        session_date (str, optional): _description_. Defaults to None.

    Returns:
        QuerySet: _description_
    """
    movie_session = MovieSession.objects.all()

    try:
        if session_date:
            movie_session = movie_session.filter(
                show_time__date=datetime.datetime.strptime(
                    session_date, "%Y-%m-%d"
                ).date()
            )
    except ValueError:
        raise ValueError("Incorrect date format. Please use 'year-month-day'")

    return movie_session


def get_movie_session_by_id(
    movie_session_id: int
) -> MovieSession:
    """_summary_
    get_movie_session_by_id, takes movie_session_id - id of the movie session,
    returns movie session with the provided id

    Args:
        movie_session_id (int): _description_

    Returns:
        MovieSession: _description_
    """
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
    session_id: int,
    show_time: datetime.datetime = None,
    movie_id: int = None,
    cinema_hall_id: int = None
) -> None:
    """_summary_
    update_movie_session, takes session_id, optional show_time, optional
    movie_id, optional cinema_hall_id. Update movie session with provided
    session_id and set fields if appropriate values are provided

    Args:
        session_id (int): _description_
        show_time (datetime.datetime, optional):
            _description_. Defaults to None.
        movie_id (int, optional): _description_. Defaults to None.
        cinema_hall_id (int, optional): _description_. Defaults to None.
    """
    movie_session = MovieSession.objects.get(id=session_id)

    if show_time:
        if isinstance(show_time, datetime.datetime):
            movie_session.show_time = show_time
        else:
            movie_session.show_time = datetime.datetime.strptime(
                show_time, "%Y-%m-%d %H:%M:%S"
            )

    if movie_id:
        movie_session.movie_id = Movie.objects.get(
            id=movie_id
        )

    if cinema_hall_id:
        movie_session.cinema_hall_id = CinemaHall.objects.get(
            id=cinema_hall_id
        )

    movie_session.save()


def delete_movie_session_by_id(
    session_id: int
) -> None:
    """_summary_
    delete_movie_session_by_id, takes session_id - id of session, deletes
    movie session with the provided id

    Args:
        session_id (int): _description_
    """
    MovieSession.objects.get(pk=session_id).delete()
