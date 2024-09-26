from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import QuerySet
from django.utils.dateparse import parse_date

from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    new_movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie=movie,
        cinema_hall=cinema_hall
    )
    return new_movie_session


def get_movies_sessions(session_date: str = None) -> QuerySet:
    if session_date:
        date_obj = parse_date(session_date)
        if not date_obj:
            raise ValueError("The date must bee format YYYY-MM-DD")
        return MovieSession.objects.filter(show_time__date=date_obj)
    else:
        return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> MovieSession:
    try:
        movie_session = MovieSession.objects.get(id=session_id)
        if show_time:
            movie_session.show_time = show_time
        if movie_id:
            movie_session.movie_id = movie_id
        if cinema_hall_id:
            movie_session.cinema_hall_id = cinema_hall_id

        movie_session.save()
        return movie_session
    except ObjectDoesNotExist:
        raise ValueError(f"Movie session with id {session_id} not found")


def delete_movie_session_by_id(session_id: int) -> bool:
    try:
        delete_session_movie = MovieSession.objects.get(id=session_id)
        delete_session_movie.delete()
        return True
    except ObjectDoesNotExist:
        return False
