from datetime import date
from typing import List

from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(movie_show_time: str,
                         movie_id: int, cinema_hall_id: int) -> None:
    session = MovieSession.objects.create(show_time=movie_show_time,
                                          cinema_hall_id=None, movie_id=None)
    session.cinema_hall_id = cinema_hall_id
    session.movie_id = movie_id

    session.save()


def get_movies_sessions(session_date: str | None = None) -> List[MovieSession]:
    if session_date:
        pars_date = session_date.split("-")
        result = MovieSession.objects.filter(
            show_time__date=date(int(pars_date[0]), int(pars_date[1]),
                                 int(pars_date[2])))

        return result
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: str = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> None:
    session = MovieSession.objects.get(id=session_id)

    if show_time:
        session.show_time = show_time

    if movie_id:
        session.movie = Movie.objects.get(id=movie_id)

    if cinema_hall_id:
        session.cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)

    session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    get_movie_session_by_id(session_id).delete()
