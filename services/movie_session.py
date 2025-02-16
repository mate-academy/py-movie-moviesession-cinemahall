from datetime import datetime
from typing import Optional
from django.db.models import QuerySet
from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(
    show_time: datetime,
    movie_id: int,
    cinema_hall_id: int
) -> MovieSession:
    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)

    return MovieSession.objects.create(
        show_time=show_time, movie=movie, cinema_hall=cinema_hall
    )


def get_movies_session(
    session_date: Optional[datetime] = None
) -> QuerySet[MovieSession]:
    query = MovieSession.objects.all()

    if session_date:
        try:
            if isinstance(session_date, datetime):
                date_obj = session_date.date()
            elif isinstance(session_date, str):
                date_obj = datetime.strptime(session_date, "%Y-%m-%d").date()
            else:
                raise ValueError("session_date must be in format YYYY-MM-DD or a datetime object.")
            query = query.filter(show_time__date=date_obj)
        except ValueError as e:
            raise ValueError(f"Invalid session_date format: {e}")

    return query


def get_movie_session_by_id(movie_session_id: int) -> QuerySet[MovieSession]:
    query = MovieSession.objects.filter(id=movie_session_id)
    return query


def update_movie_session(
    session_id: int,
    show_time: Optional[datetime] = None,
    movie_id: Optional[int] = None,
    cinema_hall_id: Optional[int] = None
) -> MovieSession:
    session = MovieSession.objects.get(id=session_id)

    if show_time is not None:
        session.movie_show_time = show_time
    if movie_id is not None:
        session.movie = Movie.objects.get(id=movie_id)
    if cinema_hall_id is not None:
        session.cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)

    session.save()
    return session


def delete_movie_session(session_id: int) -> None:
    session = MovieSession.objects.get(id=session_id)
    session.delete()
