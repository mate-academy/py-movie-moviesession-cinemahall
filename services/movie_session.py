from django.db.models import QuerySet

from datetime import datetime

from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    new_movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )
    return new_movie_session


def get_movies_sessions(
        session_date: datetime = None
) -> QuerySet:
    movie_sessions_queryset = MovieSession.objects.all()
    if session_date:
        movie_sessions_queryset = MovieSession.objects.filter(
            show_time__date=session_date
        )
    return movie_sessions_queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    if show_time:
        MovieSession.objects.filter(id=session_id).update(
            show_time=show_time
        )
    if movie_id:
        MovieSession.objects.filter(id=session_id).update(
            movie_id=movie_id
        )
    if cinema_hall_id:
        MovieSession.objects.filter(id=session_id).update(
            cinema_hall_id=cinema_hall_id
        )


def delete_movie_session_by_id(session_id: int) -> None:
    movie_session_to_delete = get_movie_session_by_id(session_id)
    movie_session_to_delete.delete()
