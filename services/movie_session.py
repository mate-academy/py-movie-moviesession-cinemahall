from datetime import datetime

from django.db.models import QuerySet

from db.models import MovieSession, CinemaHall
from services.movie import get_movie_by_id


def create_movie_session(
    movie_show_time: datetime,
    movie_id: int,
    cinema_hall_id: int
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        movie=get_movie_by_id(movie_id),
        cinema_hall=CinemaHall.objects.get(pk=cinema_hall_id),
    )


def get_movies_sessions(session_date: str = None) -> QuerySet:
    queryset = MovieSession.objects.all()
    if session_date:
        date = datetime.strptime(session_date, "%Y-%m-%d")
        date_movie_session_indices = []
        for movie_session in queryset:
            if movie_session.show_time.date() == date.date():
                date_movie_session_indices.append(movie_session.id)
        return MovieSession.objects.filter(pk__in=date_movie_session_indices)
    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(pk=movie_session_id)


def update_movie_session(
    session_id: int,
    show_time: datetime = None,
    movie_id: int = None,
    cinema_hall_id: int = None,
) -> None:
    movie_session = get_movie_session_by_id(session_id)
    if show_time:
        movie_session.show_time = show_time
    if movie_id:
        movie_session.movie = get_movie_by_id(movie_id)
    if cinema_hall_id:
        movie_session.cinema_hall = CinemaHall.objects.get(pk=cinema_hall_id)
    movie_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    get_movie_session_by_id(session_id).delete()
