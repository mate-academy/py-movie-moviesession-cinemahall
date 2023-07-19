from db.models import MovieSession, Movie, CinemaHall
from django.db.models import QuerySet

import datetime


def create_movie_session(
    movie_show_time: datetime.datetime,
    movie_id: int,
    cinema_hall_id: int,
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        movie=Movie.objects.get(id=movie_id),
        cinema_hall=CinemaHall.objects.get(id=cinema_hall_id),
    )


def get_movies_sessions(
        session_date: str = None
) -> QuerySet[MovieSession]:
    movies_session = MovieSession.objects.all()

    if session_date:
        movies_session = movies_session.filter(show_time__date=session_date)

    return movies_session


def get_movie_session_by_id(
    movie_session_id: int,
) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime.datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    if show_time:
        MovieSession.objects.filter(id=session_id).update(
            show_time=show_time
        )

    if movie_id:
        MovieSession.objects.filter(id=session_id).update(
            movie=movie_id
        )

    if cinema_hall_id:
        MovieSession.objects.filter(id=session_id).update(
            cinema_hall=cinema_hall_id
        )


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
