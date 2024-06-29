from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )
    return movie_session


def get_movies_sessions(
        session_string: str = None
) -> QuerySet:
    movies = MovieSession.objects.all()
    if session_string:
        return movies.filter(
            show_time__date=session_string
        )
    return movies


def get_movie_session_by_id(
        movie_session_id: int
) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
    session_id: int,
    cinema_hall_id: int = None,
    show_time: str = None,
    movie_id: int = None,
) -> MovieSession:
    movie_session = MovieSession.objects.filter(id=session_id)
    if cinema_hall_id:
        movie_session.update(cinema_hall=cinema_hall_id)
    if show_time:
        movie_session.update(show_time=show_time)
    if movie_id:
        movie_session.update(movie=movie_id)
    return movie_session


def delete_movie_session_by_id(
        session_id: int
) -> None:
    MovieSession.objects.get(id=session_id).delete()
