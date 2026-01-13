from db.models import MovieSession
from django.db.models import QuerySet
from datetime import datetime


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int) -> MovieSession:
    session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id)
    return session


def get_movies_sessions(
        session_date: str = None) -> QuerySet[MovieSession]:
    queryset = MovieSession.objects.all()
    if session_date:
        date_obj = datetime.strptime(
            session_date,
            "%Y-%m-%d").date()
        queryset = queryset.filter(show_time__date=date_obj)
        return queryset
    else:
        return queryset


def get_movie_session_by_id(
        movie_session_id: int) -> None | MovieSession:
    if isinstance(movie_session_id, int):
        try:
            return MovieSession.objects.get(
                id=movie_session_id)
        except MovieSession.DoesNotExist:
            return None


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None) -> None | MovieSession:
    session = get_movie_session_by_id(session_id)
    if session is None:
        return None
    if show_time:
        session.show_time = show_time
    if movie_id:
        session.movie_id = movie_id
    if cinema_hall_id:
        session.cinema_hall_id = cinema_hall_id
    session.save()
    return session


def delete_movie_session_by_id(session_id: int) -> None:
    session = get_movie_session_by_id(session_id)
    if session:
        session.delete()
