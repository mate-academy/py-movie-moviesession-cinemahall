from datetime import time, date
from db.models import MovieSession
from django.db.models import QuerySet


def create_movie_sessions(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> None:

    MovieSession.objects.create(
        show_time=time.strptime(movie_show_time, "%H:%M:%S"),
        cinema_hall=cinema_hall_id,
        movie=movie_id
    )

def get_movies_sessions(session_date: str = None) -> QuerySet:
    queryset = MovieSession.objects.all()

    if session_date:
        queryset = queryset.filter(movie__date=date.strptime(session_date,
                                                             "%Y-%m-%d"))

    return queryset

def get_movies_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)

def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    movie_session = MovieSession.objects.get(id=session_id)

    if show_time:
        movie_session.update(show_time=show_time)

    if movie_id:
        movie_session.update(movie=movie_id)

    if cinema_hall_id:
        movie_session.update(cinema_hall=cinema_hall_id)

def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
