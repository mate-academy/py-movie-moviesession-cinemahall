import warnings
from db.models import MovieSession
from datetime import time
from django.db.models import QuerySet


def create_movie_session(movie_show_time: time,
                         movie_id: int,
                         cinema_hall_id: int) -> MovieSession:
    
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(session_date: str = None) -> QuerySet:
    queryset = MovieSession.objects.all()
    if session_date:
        queryset = queryset.filter(session_date)

    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:

    if movie_session_id:
        return MovieSession.objects.get(movie_session_id)
    else:
        warnings.warn(f"""No id was provided""")


def update_movie_session(session_id: int,
                         show_time: time = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> None:
    if session_id:
        session = MovieSession.objects.get(session_id)
        if show_time:
            session.show_time = show_time
        if movie_id:
            session.movie = movie_id
        if cinema_hall_id:
            session.cinema_hall = cinema_hall_id
    else:
        warnings.warn(f"""No id was provided""")


def delete_movie_session_by_id(session_id: int = None) -> MovieSession:
    session = MovieSession.objects.get(session_id)
    return session.delete()