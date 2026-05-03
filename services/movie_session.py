from datetime import datetime, date

from django.db.models.manager import BaseManager

from db.models import MovieSession

from .movie import get_movie_by_id
from .cinema_hall import get_cinema_halls


def create_movie_session(
        movie_id: int,
        cinema_hall_id: int,
        movie_show_time: datetime
) -> MovieSession:

    movie = get_movie_by_id(movie_id)
    if not movie:
        raise ValueError(f"Movie with id {movie_id} does not exist")

    cinema_halls = get_cinema_halls()
    cinema_hall = cinema_halls.filter(id=cinema_hall_id).first()
    if not cinema_hall:
        raise ValueError(
            f"Cinema hall with id {cinema_hall_id} does not exist"
        )

    from db.models import MovieSession
    return MovieSession.objects.create(
        movie=movie,
        cinema_hall=cinema_hall,
        show_time=movie_show_time
    )


def get_movies_sessions(
        session_date: date | None = None
) -> BaseManager[MovieSession]:
    sessions = MovieSession.objects.all()

    if session_date:
        sessions = sessions.filter(show_time__date=session_date)

    return sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession | None:
    try:
        return MovieSession.objects.get(id=movie_session_id)
    except MovieSession.DoesNotExist:
        return None


def update_movie_session(
        session_id: int,
        movie_id: int | None = None,
        cinema_hall_id: int | None = None,
        show_time: datetime | None = None
) -> MovieSession:
    movie_session = get_movie_session_by_id(session_id)
    if not movie_session:
        raise ValueError(f"Movie session with id {session_id} does not exist")

    if movie_id:
        movie = get_movie_by_id(movie_id)
        if not movie:
            raise ValueError(f"Movie with id {movie_id} does not exist")
        movie_session.movie = movie

    if cinema_hall_id:
        cinema_halls = get_cinema_halls()
        cinema_hall = cinema_halls.filter(id=cinema_hall_id).first()
        if not cinema_hall:
            raise ValueError(
                f"Cinema hall with id {cinema_hall_id} does not exist"
            )
        movie_session.cinema_hall = cinema_hall

    if show_time:
        movie_session.show_time = show_time

    movie_session.save()
    return movie_session


def delete_movie_session_by_id(session_id: int) -> None:
    movie_session = get_movie_session_by_id(session_id)
    if not movie_session:
        raise ValueError(f"Movie session with id={session_id} does not exist")
    movie_session.delete()
