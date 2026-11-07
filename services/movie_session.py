from typing import Optional

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
        movie_show_time: Optional[str] = None,
        movie_id: Optional[int] = None,
        cinema_hall_id: Optional[int] = None
) -> MovieSession:
    new_movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )
    return new_movie_session


def get_movies_sessions(session_date: Optional[str] = None) -> QuerySet:
    queryset = MovieSession.objects.all()
    if session_date:
        queryset = queryset.filter(show_time__date=session_date)
    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: Optional[int] = None,
        *,
        show_time: Optional[str] = None,
        movie_id: Optional[int] = None,
        cinema_hall_id: Optional[int] = None,
) -> MovieSession:
    if session_id:
        movie_session = get_movie_session_by_id(session_id)
        if show_time:
            movie_session.show_time = show_time
        if movie_id:
            movie_session.movie_id = movie_id
        if cinema_hall_id:
            movie_session.cinema_hall_id = cinema_hall_id
        movie_session.save()
        return movie_session


def delete_movie_session_by_id(session_id: int) -> None:
    movie_session = get_movie_session_by_id(session_id)
    movie_session.delete()
