from datetime import datetime
from typing import Optional, Union

from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404

from db.models import MovieSession, CinemaHall, Movie


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    MovieSession.objects.get_or_create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(
        session_date: Optional[str] = None
) -> QuerySet[MovieSession]:
    queryset = MovieSession.objects.all()
    if session_date:
        queryset = queryset.filter(
            show_time__date=session_date)
    return queryset


def get_movie_session_by_id(
        movie_session_id: int
) -> Union[MovieSession, None]:
    return get_object_or_404(MovieSession, pk=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: Optional[datetime] = None,
        movie_id: Optional[int] = None,
        cinema_hall_id: Optional[int] = None
) -> None:
    movie_session_to_update = MovieSession.objects.get(id=session_id)

    if show_time:
        movie_session_to_update.show_time = show_time

    if movie_id:
        movie_session_to_update.movie = Movie.objects.get(id=movie_id)

    if cinema_hall_id:
        movie_session_to_update.cinema_hall = CinemaHall.objects.get(
            id=cinema_hall_id
        )

    movie_session_to_update.save()


def delete_movie_session_by_id(session_id: int) -> None:
    get_movie_session_by_id(session_id).delete()
