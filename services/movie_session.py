from typing import List

from db.models import Movie, CinemaHall, MovieSession
import datetime


def create_movie_session(movie_show_time: datetime, movie_id: Movie, cinema_hall_id: CinemaHall) -> None:
    new_movie_session = MovieSession.objects.create(show_time=movie_show_time, movie=movie_id, cinema_hall=cinema_hall_id)
    return new_movie_session


# "year-month-day"
def get_movies_sessions(session_date: str = None) -> List[MovieSession]:
    queryset = MovieSession.objects.all()
    if session_date is None:
        return queryset
    queryset = queryset.filter(show_time=session_date)  # только тут фильтр по дате?

    return queryset


def get_movie_session_by_id(movie_session_id: MovieSession) -> Movie:
    return MovieSession.objects.get(__id=movie_session_id)


def update_movie_session(session_id: MovieSession, show_time: datetime = None, movie_id: Movie = None,
                         cinema_hall_id: CinemaHall = None) -> None:
    # Person.objects.filter(id=1).update(name="Mike")
    update_movies_session = MovieSession.objects.filter(__id=session_id)
    update_movies_session.update(show_time=show_time,)
    if movie_id is not None:
        update_movies_session.movies.set(movie_id)
    if cinema_hall_id is not None:
        update_movies_session.cinema_hall.set(cinema_hall_id)


def delete_movie_session_by_id(session_id: MovieSession) -> None:
    MovieSession.objects.delete(__id=session_id)
