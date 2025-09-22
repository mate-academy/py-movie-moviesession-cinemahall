from django.db.models import QuerySet

from db.models import MovieSession, CinemaHall, Movie

import datetime


def create_movie_session(
        movie_show_time: datetime.datetime,
        cinema_hall_id: int,
        movie_id: int
) -> MovieSession:
    new_movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )

    return new_movie_session


def get_movies_sessions(session_date: str = None) -> QuerySet:
    moviesessions = MovieSession.objects.all()
    if session_date:
        session_date = datetime.datetime.strptime(
            session_date, "%Y-%m-%d"
        ).date()
        moviesessions = moviesessions.filter(show_time__date=session_date)
    return moviesessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime.datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None,
) -> None:
    session = get_movie_session_by_id(session_id)
    if show_time:
        session.show_time = show_time
    if movie_id:
        session.movie_id = movie_id
    if cinema_hall_id:
        session.cinema_hall_id = cinema_hall_id
    session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    session = get_movie_session_by_id(session_id)
    session.delete()
