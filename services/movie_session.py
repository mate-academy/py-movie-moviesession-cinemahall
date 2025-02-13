from datetime import datetime

from django.db.models.sql import Query

from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(
    movie_show_time: datetime, movie_id: int, cinema_hall_id
) -> MovieSession:
    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)

    return MovieSession.objects.create(
        movie_show_time=movie_show_time, movie=movie, cinema_hall=cinema_hall
    )


def get_movie_session(session_date: datetime | None = None) -> [Query]:
    query = MovieSession.objects.all()
    if session_date:
        try:
            date_obj = datetime.strptime(session_date, "%Y-%m-%d").date()
            query = query.filter(movie_show_time__date=date_obj)
        except ValueError:
            raise ValueError("session_date must be in format YYYY-MM-DD")

    return query


def get_movie_session_by_id(movie_session_id: int) -> [Query]:
    query = MovieSession.objects.filter(movie_session_id=movie_session_id)
    return query


def update_movie_session(
    session_id: int, show_time=None, movie_id=None, cinema_hall_id=None
) -> MovieSession:
    session = MovieSession.objects.get(id=session_id)
    if show_time is not None:
        session.movie.show_time = show_time
    if movie_id is not None:
        session.movie = Movie.objects.get(id=movie_id)
    if cinema_hall_id is not None:
        session.movie.cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)

    session.save()
    return session


def delete_movie_session(session_id: int) -> None:
    session = MovieSession.objects.get(id=session_id)
    session.delete()
