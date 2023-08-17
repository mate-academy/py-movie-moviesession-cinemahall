from typing import Optional

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(
        session_date: Optional[str] = None
) -> QuerySet[MovieSession]:
    sessions_movies = MovieSession.objects.all()

    if session_date:
        return sessions_movies.filter(show_time__date=session_date)

    return sessions_movies


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: Optional[str] = None,
        movie_id: Optional[int] = None,
        cinema_hall_id: Optional[int] = None
) -> None:
    up_session = MovieSession.objects.get(id=session_id)

    if show_time:
        up_session.show_time = show_time

    if movie_id:
        up_session.movie_id = movie_id

    if cinema_hall_id:
        up_session.cinema_hall_id = cinema_hall_id

    up_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    delete_session = get_movie_session_by_id(session_id)
    delete_session.delete()
