from datetime import datetime
from typing import Optional

from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.db.models import QuerySet
from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    movie = Movie.objects.get(id=movie_id)
    hall = CinemaHall.objects.get(id=cinema_hall_id)
    try:
        session = MovieSession.objects.create(
            show_time=movie_show_time,
            movie=movie,
            cinema_hall=hall
        )
    except IntegrityError:
        raise IntegrityError(
            "Unable to create movie session\n"
            "Arguments arent unique!"
        )
    return session


def get_movies_sessions(session_date: Optional[str] = None) -> QuerySet:
    if session_date:
        try:
            date_obj = datetime.strptime(session_date, "%Y-%m-%d").date()
            return MovieSession.objects.filter(show_time__date=date_obj)
        except ValueError:
            raise ValueError("Unknown date.", session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
    session_id: int,
    show_time: Optional[datetime] = None,
    movie_id: Optional[int] = None,
    cinema_hall_id: Optional[int] = None
) -> MovieSession:

    session = MovieSession.objects.get(id=session_id)

    if show_time is not None:
        session.show_time = show_time
    if movie_id is not None:
        session.movie = Movie.objects.get(id=movie_id)
    if cinema_hall_id is not None:
        session.cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)

    conflict_exists = MovieSession.objects.filter(
        cinema_hall=session.cinema_hall,
        movie=session.movie,
        show_time=session.show_time
    ).exclude(id=session.id).exists()

    if conflict_exists:
        raise ValidationError(
            "A movie session with actually args already exists."
        )

    session.save()
    return session


def delete_movie_session_by_id(session_id: int) -> None:
    session = MovieSession.objects.get(id=session_id)
    session.delete()
