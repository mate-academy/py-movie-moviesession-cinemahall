
import datetime

from django.db.models import QuerySet

from db.models import MovieSession, CinemaHall, Movie


def create_movie_session(movie_show_time: datetime.datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> MovieSession:
    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=cinema_hall,
        movie=movie)
    return movie_session


def get_movies_sessions(session_date: str = None) -> QuerySet[MovieSession]:
    queryset = MovieSession.objects.all()
    if session_date:
        date_obj = datetime.datetime.strptime(session_date, "%Y-%m-%d").date()
        queryset = queryset.filter(show_time__date=date_obj)
    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    queryset = MovieSession.objects.get(id=movie_session_id)
    return queryset


def update_movie_session(session_id: int,
                         show_time: datetime.datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None
                         ) -> MovieSession:
    movie_session = MovieSession.objects.get(id=session_id)
    if show_time is not None:
        movie_session.show_time = show_time
    if movie_id is not None:
        movie = Movie.objects.get(id=movie_id)
        movie_session.movie = movie
    if cinema_hall_id is not None:
        cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
        movie_session.cinema_hall = cinema_hall
    movie_session.save()
    return movie_session


def delete_movie_session_by_id(session_id: int) -> bool:
    movie_session = MovieSession.objects.get(id=session_id)
    movie_session.delete()
    return True
