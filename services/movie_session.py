from django.db.models import QuerySet
from datetime import datetime

from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int,
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id,
    )


def get_movies_sessions(
        session_date: str = None
) -> QuerySet:
    if session_date:
        target_date = datetime.strptime(session_date, "%Y-%m-%d").date()
        return MovieSession.objects.filter(
            show_time__date=target_date
        )
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None,
) -> None:
    if show_time:
        MovieSession.objects.filter(id=session_id).update(show_time=show_time)
    if movie_id:
        MovieSession.objects.filter(id=session_id).update(movie=movie_id)
    if cinema_hall_id:
        MovieSession.objects.filter(
            id=session_id).update(cinema_hall=cinema_hall_id)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
