from typing import Optional

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import QuerySet

from db.models import MovieSession, Movie, CinemaHall
from datetime import datetime


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> MovieSession:
    try:
        movie = Movie.objects.get(id=movie_id)
        cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    except ObjectDoesNotExist:
        raise ValueError("Provided movie or cinema hall ID does not exist.")

    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie=movie,
        cinema_hall=cinema_hall
    )


def get_movies_sessions(session_date: str = None) -> QuerySet[MovieSession]:
    if session_date:
        try:
            date_obj = datetime.strptime(session_date, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Invalid date format. Expected 'year-month-day'")
        return MovieSession.objects.filter(show_time__date=date_obj)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> Optional[MovieSession]:
    return MovieSession.objects.filter(id=movie_session_id).first()


def update_movie_session(session_id: int,
                         show_time: datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> bool:
    try:
        movie_session = MovieSession.objects.get(id=session_id)
    except MovieSession.DoesNotExist:
        return False

    if show_time:
        movie_session.show_time = show_time
    if movie_id:
        try:
            movie_session.movie = Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            raise ValueError("Provided movie ID does not exist.")
    if cinema_hall_id:
        try:
            movie_session.cinema_hall = CinemaHall.objects.get(
                id=cinema_hall_id)
        except CinemaHall.DoesNotExist:
            raise ValueError("Provided cinema hall ID does not exist.")

    movie_session.save()
    return True


def delete_movie_session_by_id(session_id: int) -> bool:
    deleted, _ = MovieSession.objects.filter(id=session_id).delete()
    return bool(deleted)
