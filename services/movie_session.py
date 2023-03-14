from datetime import datetime

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    new_movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )

    return new_movie_session


def get_movies_sessions(session_date: str = None) -> QuerySet(MovieSession):
    movie_session = MovieSession.objects.all()

    if session_date:
        movie_session = movie_session.filter(show_time__date=session_date)

    return movie_session


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int, **kwargs) -> MovieSession:
    session_for_update = MovieSession.objects.get(id=session_id)

    for key, value in kwargs.items():
        setattr(session_for_update, key, value)

    session_for_update.save()
    return session_for_update


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
