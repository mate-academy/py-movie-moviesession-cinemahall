from django.db.models import QuerySet
from db.models import Movie, CinemaHall, MovieSession
from datetime import datetime


def create_movie_session(movie_show_time : datetime,
                         movie_id: int,
                         cinema_hall_id: int
                         ) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(session_date: str = None) -> QuerySet:
    queryset = MovieSession.objects.all()

    if session_date:
        queryset = queryset.filter(show_time__date=session_date)
    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None
                         ) -> None:
    movie_session = MovieSession.objects.get(id=session_id)
    if isinstance(show_time, datetime):
        movie_session.show_time = show_time

    if (isinstance(movie_id, int)
            and Movie.objects.filter(id=movie_id).exists()):
        movie_session.movie_id = movie_id

    if (isinstance(cinema_hall_id, int)
            and CinemaHall.objects.filter(id=cinema_hall_id).exists()):
        movie_session.cinema_hall_id = cinema_hall_id

    movie_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
