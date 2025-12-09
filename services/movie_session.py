from datetime import datetime
from typing import Optional
from django.db.models import QuerySet
from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(
    movie_show_time: datetime,
    movie_id: int,
    cinema_hall_id: int,
) -> MovieSession:
    movie = Movie.objects.get(id=movie_id)
    hall = CinemaHall.objects.get(id=cinema_hall_id)
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie=movie,
        cinema_hall=hall,
    )


def get_movies_sessions(
    session_date: Optional[str] = None,
) -> QuerySet[MovieSession]:
    qs = MovieSession.objects.select_related("movie", "cinema_hall")

    if session_date:
        return qs.filter(show_time__date=session_date)

    return qs


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.select_related(
        "movie",
        "cinema_hall",
    ).get(id=movie_session_id)


def update_movie_session(
    session_id: int,
    show_time: Optional[datetime] = None,
    movie_id: Optional[int] = None,
    cinema_hall_id: Optional[int] = None,
) -> MovieSession:
    ms = MovieSession.objects.get(id=session_id)

    if show_time is not None:
        ms.show_time = show_time
    if movie_id is not None:
        ms.movie_id = movie_id
    if cinema_hall_id is not None:
        ms.cinema_hall_id = cinema_hall_id

    ms.save()
    return ms


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
