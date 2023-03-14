from db.models import MovieSession
from django.db.models import QuerySet


def create_movie_session(
        movie_show_time: int,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:

    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(session_date: str = None) -> QuerySet:

    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: int = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> MovieSession:

    update_session = MovieSession.objects.filter(id=session_id)

    if show_time is not None:
        update_session.update(show_time=show_time)

    if movie_id is not None:
        update_session.update(movie_id=movie_id)

    if cinema_hall_id is not None:
        update_session.update(cinema_hall_id=cinema_hall_id)

    return update_session


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
