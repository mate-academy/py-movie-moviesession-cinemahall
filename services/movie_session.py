from datetime import datetime

from django.db.models import QuerySet

from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(
        session_date: str | None = None
) -> QuerySet:
    if not session_date:
        return MovieSession.objects.all()

    return MovieSession.objects.filter(show_time__date=session_date)


def get_movie_session_by_id(
        movie_session_id: int
) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime | None = None,
        movie_id: int | None = None,
        cinema_hall_id: int | None = None
) -> None:
    session = MovieSession.objects.get(id=session_id)
    update_fields = []

    if show_time is not None:
        session.show_time = show_time
        update_fields.append("show_time")

    if movie_id is not None:
        session.movie = Movie.objects.get(id=movie_id)
        update_fields.append("movie")

    if cinema_hall_id is not None:
        session.cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
        update_fields.append("cinema_hall")

    if update_fields:
        session.save(update_fields=update_fields)


def delete_movie_session_by_id(
        session_id: int
) -> None:
    MovieSession.objects.filter(id=session_id).delete()
