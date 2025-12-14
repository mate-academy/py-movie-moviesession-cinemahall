from db.models import Movie, CinemaHall, MovieSession
from typing import Optional
from datetime import datetime
from django.utils import timezone
from django.db.models.query import QuerySet


def create_movie_session(
    movie_show_time: datetime,
    movie_id: int,
    cinema_hall_id: int
) -> MovieSession:
    if timezone.is_naive(movie_show_time):
        movie_show_time = timezone.make_aware(movie_show_time)

    movie = Movie.objects.get(id=movie_id)
    hall = CinemaHall.objects.get(id=cinema_hall_id)
    session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie=movie,
        cinema_hall=hall
    )
    return session


def get_movies_sessions(
        session_date: Optional[str] = None
) -> QuerySet[MovieSession]:
    if session_date is None:
        return MovieSession.objects.all()

    date_obj = datetime.strptime(session_date, "%Y-%m-%d").date()
    return MovieSession.objects.filter(show_time__date=date_obj)


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

    session.save()
    return session


def delete_movie_session_by_id(session_id: int) -> MovieSession:
    session = MovieSession.objects.get(id=session_id)
    session.delete()
    return session
