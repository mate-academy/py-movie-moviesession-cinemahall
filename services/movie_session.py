from django.db.models import QuerySet

from db.models import MovieSession, CinemaHall
from services.movie import get_movie_by_id


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=movie_id,
        movie=cinema_hall_id)


def get_movies_sessions(session_date: str = None) -> QuerySet:
    queryset = MovieSession.objects.all()
    if session_date:
        queryset = queryset.filter(show_time__date=session_date)
    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: str = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None
                         ) -> None:
    session_to_update = get_movie_session_by_id(session_id)

    if show_time:
        session_to_update.show_time = show_time
    if movie_id:
        movie_to_update = get_movie_by_id(movie_id)
        session_to_update.movie = movie_to_update
    if cinema_hall_id:
        cinema_hall_to_update = CinemaHall.objects.get(id=cinema_hall_id)
        session_to_update.cinema_hall = cinema_hall_to_update
    session_to_update.save()


def delete_movie_session_by_id(session_id: int) -> None:
    session_to_delete = get_movie_session_by_id(session_id)
    session_to_delete.delete()
