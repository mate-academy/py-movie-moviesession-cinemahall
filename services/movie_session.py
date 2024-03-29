from datetime import datetime

from db.models import Movie, CinemaHall, MovieSession
from services.movie import get_movie_by_id
from services.cinema_hall import get_cinema_hall_by_id


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> None | MovieSession:
    try:
        movie = Movie.objects.get(id=movie_id)
        cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    except Movie.DoesNotExist:
        return None
    return MovieSession.objects.create(show_time=movie_show_time,
                                       movie=movie,
                                       cinema_hall=cinema_hall)


def get_movies_sessions(session_date: datetime = None) -> MovieSession:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    else:
        return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> None | MovieSession:
    try:
        return MovieSession.objects.get(id=movie_session_id)
    except MovieSession.DoesNotExist:
        return None


def update_movie_session(session_id: int,
                         show_time: datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> None | MovieSession:
    try:
        session = get_movie_session_by_id(session_id)
    except MovieSession.DoesNotExist:
        return None
    if show_time:
        session.show_time = show_time
    if movie_id:
        session.movie = get_movie_by_id(movie_id) or session.movie
    if cinema_hall_id:
        session.cinema_hall = (get_cinema_hall_by_id(cinema_hall_id)
                               or session.cinema_hall)
    session.save()
    return session


def delete_movie_session_by_id(session_id: int) -> None | MovieSession:
    try:
        MovieSession.objects.get(id=session_id).delete()
    except MovieSession.DoesNotExist:
        return None
