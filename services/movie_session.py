import init_django_orm  # noqa: F401

from datetime import datetime
from django.db.models import QuerySet

from db.models import MovieSession, CinemaHall, Movie


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movies_sessions(
        session_date: str = None
) -> QuerySet:
    if session_date:
        year, month, day = session_date.split("-")
        return MovieSession.objects.filter(
            show_time__date=datetime(
                year=int(year),
                month=int(month),
                day=int(day)
            )
        )

    return MovieSession.objects.all()


def get_movie_session_by_id(
        movie_session_id: int
) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        movie_id: int = None,
        show_time: datetime = None,
        cinema_hall_id: int = None,

) -> None:
    update_movie = MovieSession.objects.get(id=session_id)
    if movie_id:
        movie = Movie.objects.get(id=movie_id)
        update_movie.movie = movie
    if show_time:
        update_movie.show_time = show_time
    if cinema_hall_id:
        cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
        update_movie.cinema_hall = cinema_hall
    update_movie.save()


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
