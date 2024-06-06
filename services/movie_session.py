from datetime import datetime
from django.db.models import QuerySet
import pytz
import init_django_orm  # noqa: F401

from db.models import Movie, CinemaHall, MovieSession

timezone = pytz.timezone("Europe/Kiev")


def create_movie_session(
        movie_show_time: type(datetime),
        movie_id: int,
        cinema_hall_id: int
) -> None:
    movie_show_time = timezone.localize(movie_show_time)
    movie_session = MovieSession(
        show_time=movie_show_time,
        movie=Movie.objects.get(id=movie_id),
        cinema_hall=CinemaHall.objects.get(id=cinema_hall_id)
    )
    movie_session.save()


def get_movies_sessions(session_date: type(datetime) = None) -> QuerySet:
    movie_sessions = MovieSession.objects.all()
    if session_date:
        session_date = datetime.strptime(session_date, "%Y-%m-%d")
        session_date = timezone.localize(session_date)
        movie_sessions = movie_sessions.filter(show_time__date=session_date)
    return movie_sessions


def get_movie_session_by_id(movie_session_id: int) -> None:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: type(datetime) = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    movie_session = MovieSession.objects.get(id=session_id)
    if show_time:
        show_time = timezone.localize(show_time)
        movie_session.show_time = show_time
    if movie_id:
        movie_session.movie = Movie.objects.get(id=movie_id)
    if cinema_hall_id:
        movie_session.cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    movie_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id) .delete()
