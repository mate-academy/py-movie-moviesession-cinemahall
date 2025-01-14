from datetime import datetime

from django.db.models import QuerySet

from db.models import MovieSession, CinemaHall, Movie


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    movie_session = MovieSession(
        show_time=movie_show_time,
        cinema_hall=CinemaHall.objects.get(id=cinema_hall_id),
        movie=Movie.objects.get(id=movie_id),
    )
    movie_session.save()
    return movie_session


def get_movies_sessions(session_date: datetime = None) -> QuerySet:
    if session_date is not None:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> MovieSession:
    movie_session = get_movie_session_by_id(session_id)

    if show_time is not None:
        movie_session.show_time = show_time

    if movie_id is not None:
        movie_session.movie_id = Movie.objects.get(id=movie_id)

    if cinema_hall_id is not None:
        movie_session.cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)

    movie_session.save()

    return movie_session


def delete_movie_session(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
