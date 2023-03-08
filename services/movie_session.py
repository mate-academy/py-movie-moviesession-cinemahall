from datetime import datetime

from django.db.models import QuerySet

from db.models import MovieSession, CinemaHall
from services.movie import get_movie_by_id


def create_movie_session(
    movie_show_time: str,
    movie_id: int,
    cinema_hall_id: int,
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=CinemaHall.objects.get(id=cinema_hall_id),
        movie=get_movie_by_id(movie_id),
    )


def get_movies_sessions(session_date: str = None) -> QuerySet[MovieSession]:
    queryset = MovieSession.objects.all()
    if session_date:
        movie_session_time = datetime.strptime(session_date, "%Y-%m-%d")
        queryset = queryset.filter(show_time__date=movie_session_time)
    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
    session_id: int,
    show_time: str = None,
    movie_id: int = None,
    cinema_hall_id: int = None,
) -> None:
    movie_session_to_update = get_movie_session_by_id(session_id)
    if show_time:
        movie_session_to_update.show_time = show_time
    if cinema_hall_id:
        movie_session_to_update.cinema_hall = CinemaHall.objects.get(
            id=cinema_hall_id
        )
    if movie_id:
        movie_session_to_update.movie = get_movie_by_id(movie_id)
    movie_session_to_update.save()


def delete_movie_session_by_id(session_id: int) -> None:
    get_movie_session_by_id(movie_session_id=session_id).delete()
