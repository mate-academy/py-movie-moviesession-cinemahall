from db.models import MovieSession, CinemaHall, Movie
import datetime
from django.db.models import QuerySet


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> MovieSession:
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    movie = Movie.objects.get(id=movie_id)
    movie_session = MovieSession.objects.create(show_time=movie_show_time,
                                                cinema_hall=cinema_hall,
                                                movie=movie)
    return movie_session


def get_movies_sessions(
    session_date: datetime = None
) -> QuerySet[MovieSession]:
    if session_date:
        date = datetime.datetime.strptime(session_date, "%Y-%m-%d")
        movie_sessions = MovieSession.objects.filter(show_time__date=date)
    else:
        movie_sessions = MovieSession.objects.all()

    return movie_sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    movie_session = MovieSession.objects.get(id=movie_session_id)
    return movie_session


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int | None = None,
        cinema_hall_id: int | None = None
) -> MovieSession:
    movie_session = MovieSession.objects.get(id=session_id)
    if show_time:
        movie_session.show_time = show_time
    if movie_id:
        movie_session.movie = Movie.objects.get(id=movie_id)
    if cinema_hall_id:
        movie_session.cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    movie_session.save()

    return movie_session


def delete_movie_session_by_id(session_id: int) -> None:
    movie_session = MovieSession.objects.get(id=session_id)
    movie_session.delete()
