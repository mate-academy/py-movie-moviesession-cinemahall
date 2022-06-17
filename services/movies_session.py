from db.models import MovieSession
from datetime import datetime


def create_movie_session(
        movie_show_time,
        movie_id: int,
        cinema_hall_id: int
):
    new_movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )
    return new_movie_session


def get_movies_sessions(session_date: str = None):
    queryset = MovieSession.objects.all()

    if session_date:
        session_date = datetime.strptime(session_date, "%Y-%m-%d")
        queryset = queryset.filter(show_time__date=session_date)

    return queryset


def get_movie_session_by_id(movie_session_id: int):

    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time=None,
        movie_id: int = None,
        cinema_hall_id: int = None
):

    session_to_update = MovieSession.objects.filter(id=session_id)

    if show_time:
        session_to_update.update(show_time=show_time)

    if movie_id:
        session_to_update.update(movie_id=movie_id)

    if cinema_hall_id:
        session_to_update.update(cinema_hall_id=cinema_hall_id)

    return session_to_update


def delete_movie_session_by_id(session_id: int):
    return MovieSession.objects.filter(id=session_id).delete()
