from django.db.models import QuerySet
from django.utils.datetime_safe import datetime
from django.shortcuts import get_object_or_404

from db.models import MovieSession, CinemaHall, Movie


def create_movie_session(
    movie_show_time: datetime,
    movie_id: int,
    cinema_hall_id: int
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=get_object_or_404(CinemaHall, id=cinema_hall_id),
        movie=get_object_or_404(Movie, id=movie_id)
    )


def get_movies_sessions(session_time: str = None) -> QuerySet[MovieSession]:
    queryset = MovieSession.objects.all()
    if session_time:
        date = datetime.strptime(session_time, "%Y-%m-%d")
        queryset = queryset.filter(show_time__date=date)
    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return get_object_or_404(MovieSession, id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    movie = get_object_or_404(MovieSession, id=session_id)
    if show_time:
        movie.show_time = show_time
    if movie_id:
        movie.movie = (Movie.objects.get(id=movie_id))
    if cinema_hall_id:
        movie.cinema_hall = (CinemaHall.objects.get(id=cinema_hall_id))

    movie.save()


def delete_movie_session_by_id(session_id: int) -> None:
    get_object_or_404(MovieSession, id=session_id).delete()
