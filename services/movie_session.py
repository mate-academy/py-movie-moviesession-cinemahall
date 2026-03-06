from django.db.models import QuerySet
import datetime
from db.models import MovieSession


def create_movie_session(movie_show_time=datetime|None, movie_id=None,
                         cinema_hall_id=None) -> QuerySet:
    create = MovieSession.create(movie_show_time=movie_show_time,
                                 movie_id=movie_id, cinema_hall_id=cinema_hall_id)
    return create

def get_movies_sessions(session_date=str|None) -> QuerySet:
    queryset = MovieSession.all()
    if session_date:
        queryset = queryset.filter(show_time__date=session_date)
        return queryset

def get_movie_session_by_id(movie_session_id=None) -> QuerySet:
    return MovieSession.filter(id=movie_session_id).all()

def update_movie_session(session_id=None, show_time=None,
                         movie_id=None, cinema_hall_id=None) -> QuerySet:
    session = MovieSession.objects.get(id=session_id)
    if show_time is not None:
        session.show_time = show_time
    if movie_id is not None:
        session.movie_id = movie_id
    if cinema_hall_id is not None:
        session.cinema_hall_id = cinema_hall_id
        session.save()

def delete_movie_session_by_id(session_id=None) -> QuerySet:
    return MovieSession.filter(id=session_id).delete()
