import datetime

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(movie_show_time: datetime.date,
                         movie_id: int,
                         cinema_hall_id: int) -> MovieSession:
    session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id)
    return session


def get_movies_sessions(
        session_date: str | None = None) -> QuerySet:
    queryset = MovieSession.objects.select_related("movie", "cinema_hall")
    if session_date:
        queryset = queryset.filter(show_time__date=session_date)
    queryset = queryset.order_by(
        "show_time",
        "cinema_hall__name",
        "movie__title"
    )
    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    session = MovieSession.objects.get(id=movie_session_id)
    return session


def update_movie_session(
        session_id: int,
        show_time: int = None,
        movie_id: int = None,
        cinema_hall_id: int = None) -> MovieSession:
    session = MovieSession.objects.get(id=session_id)
    if show_time is not None:
        session.show_time = show_time
    if movie_id is not None:
        session.movie_id = movie_id
    if cinema_hall_id is not None:
        session.cinema_hall_id = cinema_hall_id
    session.save()
    return session


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
