import datetime

from db.models import MovieSession

from django.db.models import QuerySet


def create_movie_session(
        movie_show_time: datetime.datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(session_date: str = None) -> QuerySet:
    all_sessions = MovieSession.objects.all()
    if session_date is not None:
        all_sessions = all_sessions.filter(show_time__date=session_date)
    return all_sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime.datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    new_move_session = MovieSession.objects.get(id=session_id)

    if show_time is not None:
        new_move_session.show_time = show_time

    if movie_id is not None:
        new_move_session.movie_id = movie_id

    if cinema_hall_id is not None:
        new_move_session.cinema_hall_id = cinema_hall_id

    new_move_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
