from django.db.models import QuerySet
from db.models import MovieSession
from datetime import datetime


def create_movie_session(
    movie_show_time: datetime,
    movie_id: int,
    cinema_hall_id: int
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(session_date: str = None) -> QuerySet:

    if session_date:
        parsed_date = session_date.split("-")
        return MovieSession.objects.filter(
            show_time__year=parsed_date[0],
            show_time__month=parsed_date[1],
            show_time__day=parsed_date[2]
        )
    else:
        return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
    session_id: int,
    show_time: datetime = None,
    movie_id: int = None,
    cinema_hall_id: int = None
) -> None:

    session_to_update = MovieSession.objects.filter(id=session_id)

    if show_time:
        session_to_update.update(show_time=show_time)
    if movie_id:
        session_to_update.update(movie_id=movie_id)
    if cinema_hall_id:
        session_to_update.update(cinema_hall_id=cinema_hall_id)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
