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


def update_movie_session(session_id: int, **kwargs: dict) -> None:
    session_to_update = get_movie_session_by_id(session_id)

    for attr, value in kwargs.items():
        if value is not None:
            setattr(session_to_update, attr, value)

    session_to_update.save()


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
