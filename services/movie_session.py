from datetime import datetime
from typing import Optional

from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(movie_show_time: datetime, movie_id: int, cinema_hall_id: int):
    MovieSession.objects.create(
        show_time=movie_show_time, movie=Movie.objects.get(pk=movie_id),
        cinema_hall=CinemaHall.objects.get(pk=cinema_hall_id)
    )


def get_movies_sessions(session_date: Optional[str] = None):
    if session_date:
        search_date = datetime.strptime(session_date, "%Y-%m-%d")
        return MovieSession.objects.filter(show_time__date=search_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int):
    return MovieSession.objects.get(pk=movie_session_id)


def update_movie_session(
        session_id: int, show_time: Optional[datetime] = None,
        movie_id: Optional[int] = None, cinema_hall_id: Optional[int] = None
):
    movie_session = MovieSession.objects.get(pk=session_id)

    if show_time:
        movie_session.show_time = show_time

    if movie_id:
        movie_session.movie_id = movie_id

    if cinema_hall_id:
        movie_session.cinema_hall_id = cinema_hall_id

    movie_session.save()


def delete_movie_session_by_id(session_id: int):
    MovieSession.objects.filter(pk=session_id).delete()
