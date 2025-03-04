from db.models import MovieSession
import datetime
from typing import List


def create_movie_session(movie_show_time: datetime.datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> None:
    MovieSession.objects.create(show_time=movie_show_time,
                                movie_id=movie_id,
                                cinema_hall_id=cinema_hall_id)


def get_movies_sessions(session_date: str = None) -> List[MovieSession]:
    if session_date:
        return MovieSession.objects.filter(show_time=session_date)
    else:
        return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.filter(id__in=movie_session_id)


def update_movie_session(session_id: int, show_time: datetime.datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> MovieSession:
    session = MovieSession.objects.get(id=session_id)
    if show_time is not None:
        session.show_time = show_time
    if movie_id is not None:
        session.movie = movie_id
    if cinema_hall_id is not None:
        session.cinema_hall = cinema_hall_id
    session.save()
    return session


def delete_movie_session_by_id(session_id):
    return MovieSession.objects.delete(id=session_id)
