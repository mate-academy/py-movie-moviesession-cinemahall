from datetime import datetime

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime,
        cinema_hall_id: int,
        movie_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movies_sessions(
        session_date: datetime | None = None
) -> QuerySet:

    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime | None = None,
        cinema_hall_id: int | None = None,
        movie_id: int | None = None
) -> MovieSession:
    movie_session = get_movie_session_by_id(session_id)

    if show_time is not None:
        movie_session.show_time = show_time
    if cinema_hall_id is not None:
        movie_session.cinema_hall_id = cinema_hall_id
    if movie_id is not None:
        movie_session.movie_id = movie_id

    movie_session.save()

    return movie_session


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
