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


def get_movies_sessions(session_date: str = None) -> QuerySet:
    if session_date is None:
        return MovieSession.objects.all()
    return MovieSession.objects.filter(show_time__date=session_date)


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int, **kwargs) -> MovieSession:
    movie_session = MovieSession.objects.get(id=session_id)
    for key, value in kwargs.items():
        if hasattr(movie_session, key):
            setattr(movie_session, key, value)
    movie_session.save()
    return movie_session


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get_movie_session_by_id(session_id).delete()
