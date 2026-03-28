from typing import Optional
from db.models import MovieSession
from django.db.models import QuerySet
from datetime import datetime


def create_movie_session(movie_show_time: datetime, movie_id: int,
                         cinema_hall_id: int) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(session_date: Optional[str] = None) -> QuerySet:
    queryset = MovieSession.objects.all()
    if session_date:
        try:
            date_obj = datetime.strptime(session_date, "%Y-%m-%d")
        except ValueError:
            date_obj = datetime.strptime(session_date, "%Y-%-m-%d")
        queryset = queryset.filter(show_time__date=date_obj)
    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int, show_time: Optional[datetime] = None,
                         movie_id: Optional[int] = None,
                         cinema_hall_id: Optional[int] = None
                         ) -> MovieSession:
    session = MovieSession.objects.get(id=session_id)
    if show_time:
        session.show_time = show_time
    if movie_id:
        session.movie_id = movie_id
    if cinema_hall_id:
        session.cinema_hall_id = cinema_hall_id
    session.save()
    return session


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
