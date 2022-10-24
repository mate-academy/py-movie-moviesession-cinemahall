import init_django_orm  # noqa: F401
from db.models import MovieSession
from datetime import datetime
from django.db.models import QuerySet


def get_movies_sessions(session_date: datetime = None) -> QuerySet:
    queryset = MovieSession.objects.all()

    if session_date:
        queryset = queryset.filter(show_time__date=session_date)

    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    movie_by_id = MovieSession.objects.get(id=movie_session_id)
    return movie_by_id


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> MovieSession:
    updated_movie_session = MovieSession.objects.get(id=session_id)

    if show_time:
        updated_movie_session.show_time = show_time

    if movie_id:
        updated_movie_session.movie_id = movie_id

    if cinema_hall_id:
        updated_movie_session.cinema_hall_id = cinema_hall_id
    updated_movie_session.save()
    return updated_movie_session


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


def delete_movie_session_by_id(session_id: int) -> tuple[int, dict]:
    return MovieSession.objects.get(id=session_id).delete()


print(delete_movie_session_by_id(1))
