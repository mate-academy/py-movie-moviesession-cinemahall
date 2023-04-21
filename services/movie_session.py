from datetime import datetime

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
    movie_show_time: datetime,
    movie_id: int,
    cinema_hall_id: int,
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id,
    )


def get_movies_sessions(session_date: str = None) -> QuerySet:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(pk=movie_session_id)


def update_movie_session(
    session_id: int,
    show_time: datetime = None,
    movie_id: int = None,
    cinema_hall_id: int = None,
) -> None:
    session = MovieSession.objects.get(pk=session_id)
    fields = {
        "show_time": show_time,
        "movie_id": movie_id,
        "cinema_hall_id": cinema_hall_id,
    }
    for name, field in fields.items():
        if field:
            setattr(session, name, field)
    session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(pk=session_id).delete()
