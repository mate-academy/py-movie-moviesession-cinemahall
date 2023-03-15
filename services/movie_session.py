from django.db.models import QuerySet

import init_django_orm  # noqa: F401
from db.models import MovieSession


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:

    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movies_sessions(session_date: str = None) -> QuerySet:
    sessions = MovieSession.objects.all()

    if session_date:
        sessions = MovieSession.objects.filter(
            show_time__date=session_date
        )

    return sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> MovieSession:
    session_to_update = MovieSession.objects.get(id=session_id)
    if show_time:
        session_to_update.show_time = show_time
    if movie_id:
        session_to_update.movie_id = movie_id
    if cinema_hall_id:
        session_to_update.cinema_hall_id = cinema_hall_id
    session_to_update.save()

    return session_to_update


def delete_movie_session_by_id(section_id: int) -> MovieSession:
    return MovieSession.objects.get(id=section_id).delete()
