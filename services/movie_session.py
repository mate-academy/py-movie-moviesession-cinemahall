from db.models import MovieSession
from services.movie import get_movie_by_id
from services.cinema_hall import get_cinema_hall_by_id


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession.objects:
    new_session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=get_cinema_hall_by_id(cinema_hall_id),
        movie=get_movie_by_id(movie_id)
    )

    return new_session


def get_movies_sessions(session_date: str = None) -> MovieSession.objects:
    queryset = MovieSession.objects.all()

    if session_date is not None:
        queryset = queryset.filter(show_time__date=session_date)

    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession.objects:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> MovieSession.objects:
    update_session = get_movie_session_by_id(session_id)

    if show_time is not None:
        update_session.show_time = show_time

    if movie_id is not None:
        update_session.movie_id = movie_id

    if cinema_hall_id is not None:
        update_session.cinema_hall_id = cinema_hall_id

    update_session.save()
    return update_session


def delete_movie_session_by_id(session_id: int) -> None:
    get_movie_session_by_id(session_id).delete()
