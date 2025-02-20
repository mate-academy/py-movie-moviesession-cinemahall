from db.models import MovieSession
from django.db.models import QuerySet
import datetime


def create_movie_session(
        movie_show_time: datetime.datetime,
        movie_id: int,
        cinema_hall_id: int,
) -> None:
    MovieSession.objects.create(
        movie_id=movie_id,
        show_time=movie_show_time,
        cinema_hall=cinema_hall_id,
    )


def get_movies_sessions(session_date: str = None) -> QuerySet:
    movies_sessions = MovieSession.objects.all()
    if session_date:
        movies_sessions = movies_sessions.filter(
            show_time__date=session_date
        )

    return movies_sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    try:
        movie_session = MovieSession.objects.get(
            id=movie_session_id
        )

        return movie_session
    except MovieSession.DoesNotExist:
        return None


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None,
) -> None:
    movie_session = get_movie_session_by_id(session_id)

    if not movie_session:
        raise MovieSession.DoesNotExist("Movie session not found.")

    if show_time:
        movie_session.show_time = show_time

    if movie_id:
        movie_session.movie_id = movie_id

    if cinema_hall_id:
        movie_session.cinema_hall_id = cinema_hall_id

    movie_session.save()


def delete_movie_session(session_id: int) -> None:
    try:
        movie_session = MovieSession.objects.get(id=session_id)
        movie_session.delete()
    except MovieSession.DoesNotExist:
        raise Exception("Movie session not found.")
