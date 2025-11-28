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
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movies_sessions(session_date: str = None) -> QuerySet[MovieSession]:

    query_set = MovieSession.objects.all()
    if session_date:
        query_set = query_set.filter(show_time__date=session_date)
    return query_set


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime | None = None,
        movie_id: int | None = None,
        cinema_hall_id: int | None = None
) -> MovieSession:

    query_set = MovieSession.objects.get(id=session_id)
    if show_time:
        query_set.show_time = show_time
    if movie_id:
        query_set.movie_id = movie_id
    if cinema_hall_id:
        query_set.cinema_hall_id = cinema_hall_id
    query_set.save()
    return query_set


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
