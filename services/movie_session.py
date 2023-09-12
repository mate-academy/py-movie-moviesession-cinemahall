from datetime import datetime

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
    movie_show_time: datetime,
    movie_id: int,
    cinema_hall_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(
        session_date: datetime = None
) -> QuerySet[MovieSession]:
    if session_date is None:
        return MovieSession.objects.all()
    return MovieSession.objects.filter(show_time__date=session_date)


def get_movie_session_by_id(movie_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    update_movie_session_ = MovieSession.objects.get(id=session_id)

    if show_time:
        update_movie_session_.show_time = show_time

    if movie_id:
        update_movie_session_.movie_id = movie_id

    if cinema_hall_id:
        update_movie_session_.cinema_hall_id = cinema_hall_id

    update_movie_session_.save()


def delete_movie_session_by_id(session_id: int) -> MovieSession:
    MovieSession.objects.get(id=session_id).delete()
