import datetime

from django.db.models import QuerySet

from db.models import MovieSession, CinemaHall, Movie


def create_movie_session(
    movie_show_time: datetime, movie_id: int, cinema_hall_id: int
) -> QuerySet:
    new_movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=CinemaHall.objects.get(id=cinema_hall_id),
        movie=Movie.objects.get(id=movie_id),
    )
    return new_movie_session


def get_movies_sessions(session_date: str = None) -> QuerySet:
    movie_session_query = MovieSession.objects.all()

    if session_date is not None:
        movie_session_query = movie_session_query.filter(
            show_time__date=session_date
        )

    return movie_session_query


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
    session_id: int,
    show_time: str = None,
    movie_id: int = None,
    cinema_hall_id: int = None,
) -> MovieSession:
    movie_session = MovieSession.objects.all()
    movie_session = movie_session.filter(id=session_id)

    if show_time is not None:
        movie_session.update(show_time=show_time)

    if movie_id is not None:
        movie_session.update(movie=movie_id)

    if cinema_hall_id is not None:
        movie_session.update(cinema_hall=cinema_hall_id)

    return movie_session


def delete_movie_session_by_id(session_id: int) -> None:
    movie_session = MovieSession.objects.all()
    return movie_session.filter(id=session_id).delete()
