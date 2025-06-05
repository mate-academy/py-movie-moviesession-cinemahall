from django.db.models import QuerySet
from db.models import MovieSession
import datetime


def create_movie_session(movie_show_time: datetime.datetime,
                         movie_id: int, cinema_hall_id: int) -> None:
    MovieSession.objects.create(show_time=movie_show_time,
                                movie_id=movie_id,
                                cinema_hall_id=cinema_hall_id)


def get_movies_sessions(session_date: datetime.datetime = None) -> QuerySet:
    mm = MovieSession.objects.all()
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    else:
        return mm

# test commit

def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int, show_time: datetime.datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> None:
    kk = MovieSession.objects.get(id=session_id)
    if show_time:
        kk.show_time = show_time
    if movie_id:
        kk.movie_id = movie_id
    if cinema_hall_id:
        kk.cinema_hall_id = cinema_hall_id
    kk.save()


def delete_movie_session_by_id(session_id: int) -> None:
    rr = MovieSession.objects.get(id=session_id)
    rr.delete()
