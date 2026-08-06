from datetime import datetime

from django.db.models import QuerySet

from db.models import Movie, CinemaHall, MovieSession


def create_movie_session(
    movie_show_time: datetime,
    movie_id: int,
    cinema_hall_id: int
) -> MovieSession:
    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=cinema_hall,
        movie=movie
    )


def get_movies_sessions(
    session_date: str | None = None
) -> QuerySet:
    if session_date:
        return MovieSession.objects.filter(
            show_time__date=session_date
        )
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession | None:
    return MovieSession.objects.filter(id=movie_session_id).first()


def update_movie_session(
    session_id: int,
    show_time: datetime | None = None,
    movie_id: int | None = None,
    cinema_hall_id: int | None = None,
) -> int:
    update = {}
    if show_time is not None:
        update["show_time"] = show_time
    if cinema_hall_id is not None:
        update["cinema_hall"] = cinema_hall_id
    if movie_id is not None:
        update["movie"] = movie_id
    return MovieSession.objects.filter(id=session_id).update(**update)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
