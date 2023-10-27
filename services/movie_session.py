from db.models import MovieSession
from datetime import datetime


def create_movie_session(movie_show_time: datetime, movie_id: int):
    pass


def get_movies_sessions(session_date: str = None):
    pass


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    pass


def update_movie_session(session_id: int,
                         show_time: datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> None:
    pass


def delete_movie_session_by_id(session_id: int) -> None:
    pass