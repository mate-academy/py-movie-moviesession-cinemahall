from datetime import datetime
from django.db.models import QuerySet
from db.models import Movie, CinemaHall, MovieSession


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> MovieSession:
    if movie_show_time and movie_id and cinema_hall_id:
        cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
        movie = Movie.objects.get(id=movie_id)
        movie_session = MovieSession(
            show_time=movie_show_time,
            cinema_hall=cinema_hall,
            movie=movie
        )
        movie_session.save()
        return movie_session


def get_movies_sessions(session_date: str = None) -> QuerySet | MovieSession:
    query_set = MovieSession.objects.all()
    if session_date:
        query_set = query_set.filter(show_time__date=session_date)
    return query_set


def get_movie_session_by_id(movie_session_id: id) -> MovieSession:
    if movie_session_id:
        movie_session = MovieSession.objects.get(id=movie_session_id)
        return movie_session


def update_movie_session(session_id: int, show_time: str = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> MovieSession:
    if session_id:
        movie_session = MovieSession.objects.get(id=session_id)
    if show_time:
        movie_session.show_time = show_time
    if movie_id:
        movie = Movie.objects.get(id=movie_id)
        movie_session.movie = movie
    if cinema_hall_id:
        cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
        movie_session.cinema_hall = cinema_hall
    movie_session.save()


def delete_movie_session_by_id(session_id: int) -> MovieSession:
    if session_id:
        movie_session = MovieSession.objects.filter(id=session_id).delete()
        return movie_session
