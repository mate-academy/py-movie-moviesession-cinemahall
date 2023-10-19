import datetime
from db.models import MovieSession, Movie, CinemaHall
from django.db.models.query import QuerySet
from typing import Optional


def create_movie_session(
        movie_show_time: datetime.datetime,
        movie_id: int,
        cinema_hall_id: int
) -> QuerySet[MovieSession]:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movies_sessions(
        session_date: Optional[datetime.date] = None
) -> QuerySet[MovieSession]:
    queryset = MovieSession.objects.all()

    if session_date:
        queryset = queryset.filter(show_time__date=session_date)

    return queryset


def get_movie_session_by_id(movie_session_id: int) -> QuerySet[MovieSession]:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: Optional[str] = None,
        movie_id: Optional[int] = None,
        cinema_hall_id: Optional[int] = None
) -> None:
    movie_session_to_update = get_movie_session_by_id(session_id)
    if show_time:
        movie_session_to_update.show_time = show_time

    if movie_id is not None:
        movie = Movie.objects.get(id=movie_id)
        movie_session_to_update.movie = movie

    if cinema_hall_id is not None:
        cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
        movie_session_to_update.cinema_hall = cinema_hall

    movie_session_to_update.save()


def delete_movie_session_by_id(session_id: int) -> None:
    movie_session_to_delete = get_movie_session_by_id(session_id)
    movie_session_to_delete.delete()
