import django.db.models.query
import init_django_orm  #noqa:F401

import datetime
from db.models import MovieSession


def create_movie_session(movie_show_time, movie_id, cinema_hall_id):
    return MovieSession.objects.create(
       movie=movie_id,
       cinema_hall=cinema_hall_id,
       show_time=movie_show_time,
    )


def get_movies_sessions(session_date=None):
    sessions = MovieSession.objects.all()
    if session_date is not None:
        sessions = sessions.filter(show_time__date=session_date)
    return sessions


def get_movie_session_by_id(movie_session_id):
    return MovieSession.objects.filter(id=movie_session_id)


def update_movie_session(session_id: int, show_time: datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None):
    session_ = MovieSession.objects.filter(id=session_id)
    if show_time is not None:
        session_.show_time = show_time
    if movie_id is not None:
        session_.movie_id = movie_id
    if cinema_hall_id is not None:
        session_.cinema_hall_id = cinema_hall_id


def delete_movie_session_by_id(session_id):
    MovieSession.objects.filter(id=session_id).delete()


if __name__ == '__main__':
    pass
