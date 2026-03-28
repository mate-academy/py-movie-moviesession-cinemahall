from datetime import datetime

from django.db.models.query import QuerySet

from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(session_date: str = None) -> QuerySet:
    movie_sessions = MovieSession.objects.all()
    if session_date:
        movie_sessions = movie_sessions.filter(show_time__date=session_date)
    return movie_sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: str | None = None,
                         movie_id: int | None = None,
                         cinema_hall_id: int | None = None) -> None:
    session = MovieSession.objects.filter(id=session_id)

    if show_time:
        session.update(show_time=show_time)
    if movie_id:
        movie = Movie.objects.get(id=movie_id)
        session.update(movie=movie)
    if cinema_hall_id:
        hall = CinemaHall.objects.get(id=cinema_hall_id)
        session.update(cinema_hall=hall)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
