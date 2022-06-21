from datetime import datetime

from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
):
    movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )

    return movie_session


def get_movies_sessions(session_date: str = None):
    query = MovieSession.objects.all()

    if session_date is not None:
        date_session = session_date.split("-")
        query = query.filter(
            show_time__year=date_session[0],
            show_time__month=date_session[1],
            show_time__day=date_session[2]
        )

    return query


def get_movie_session_by_id(movie_session_id: int):
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None,
):
    movie_session_to_update = MovieSession.objects.filter(id=session_id)

    if movie_id:
        movie_session_to_update.update(movie_id=movie_id)

    if cinema_hall_id:
        movie_session_to_update.update(cinema_hall_id=cinema_hall_id)

    if show_time is not None:
        movie_session_to_update.update(show_time=show_time)

    return movie_session_to_update


def delete_movie_session_by_id(session_id: int):
    MovieSession.objects.filter(id=session_id).delete()
