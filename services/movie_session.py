from datetime import datetime
from db.models import MovieSession
from django.db.models import QuerySet


def create_movie_session(
    movie_show_time: datetime,
    movie_id: int,
    cinema_hall_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(session_date: str = None) -> QuerySet[MovieSession]:
    movies_sessions = MovieSession.objects.all()
    if session_date is not None:
        movies_sessions = movies_sessions.filter(show_time__date=session_date)
    return movies_sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def if_is_not_none_update_attr(
    session: MovieSession,
    attribute: str,
    value: int | datetime
) -> MovieSession:
    if value is not None:
        setattr(session, attribute, value)
    return session


def update_movie_session(
    session_id: int,
    show_time: datetime = None,
    movie_id: int = None,
    cinema_hall_id: int = None
) -> None:
    movie_session = MovieSession.objects.get(id=session_id)
    if_is_not_none_update_attr(movie_session, "show_time", show_time)
    if_is_not_none_update_attr(movie_session, "movie_id", movie_id)
    if_is_not_none_update_attr(
        movie_session, "cinema_hall_id", cinema_hall_id
    )
    movie_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
