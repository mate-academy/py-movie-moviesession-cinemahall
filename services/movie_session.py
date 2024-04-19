import init_django_orm  # noqa: F401

from db.models import MovieSession


def create_movie_session(movie_show_time: str,
                         movie_id: int, cinema_hall_id: int) -> None:
    MovieSession.objects.create(show_time=movie_show_time,
                                movie_id=movie_id,
                                cinema_hall_id=cinema_hall_id)


def get_movies_sessions(session_date: str = None) -> MovieSession:
    filters = {}

    if session_date:
        filters["show_time__date"] = session_date

    return MovieSession.objects.filter(**filters)


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: str = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> None:
    update_movie = {}

    if show_time:
        update_movie["show_time"] = show_time

    if movie_id:
        update_movie["movie"] = movie_id

    if cinema_hall_id:
        update_movie["cinema_hall"] = cinema_hall_id
    MovieSession.objects.filter(id=session_id).update(
        **update_movie
    )


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
