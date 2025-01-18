from datetime import datetime
from django.db.models import QuerySet
from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=cinema_hall,
        movie=movie
    )


def get_movies_sessions(session_date: str = None) -> QuerySet:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    else:
        return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> MovieSession:
    updated = get_movie_session_by_id(session_id)
    if show_time:
        updated.show_time = show_time
    if movie_id:
        updated.movie = Movie.objects.get(id=movie_id)
    if cinema_hall_id:
        updated.cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    updated.save()
    return updated


def delete_movie_session_by_id(session_id: int) -> None:
    get_movie_session_by_id(session_id).delete()
