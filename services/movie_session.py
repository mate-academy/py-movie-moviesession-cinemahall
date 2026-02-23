from datetime import datetime

from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int = None,
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id,
    )


def get_movies_sessions(session_date: str = None) -> list[MovieSession]:
    if not session_date:
        return MovieSession.objects.all()

    return MovieSession.objects.filter(show_time__date=session_date)


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movies_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None,
) -> MovieSession:
    props_to_update = {}

    if show_time:
        props_to_update['show_time'] = show_time

    if movie_id:
        props_to_update['movie_id'] = movie_id

    if cinema_hall_id:
        props_to_update['cinema_hall_id'] = cinema_hall_id

    return MovieSession.objects.filter(id=session_id).update(**props_to_update)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
