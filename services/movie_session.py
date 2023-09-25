from typing import List

from db.models import Movie, CinemaHall, MovieSession
import datetime


def create_movie_session(movie_show_time: datetime, movie_id: Movie, cinema_hall_id: CinemaHall) -> None:
    pass


# "year-month-day"
def get_movies_sessions(session_date: str = None) -> List[MovieSession]:
    pass


def get_movie_session_by_id(movie_session_id: MovieSession) -> Movie:
    pass


def update_movie_session(session_id: MovieSession, show_time: datetime = None, movie_id: Movie = None,
                         cinema_hall_id: CinemaHall = None) -> None:
    pass


def delete_movie_session_by_id(session_id: MovieSession) -> None:
    pass
