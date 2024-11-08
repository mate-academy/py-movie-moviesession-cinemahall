from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

import init_django_orm  # noqa: F401
from db.models import MovieSession, CinemaHall, Movie


def create_movie_session(movie_show_time: str,
                         movie_id: int,
                         cinema_hall_id: int) -> MovieSession:
    cinema_hall = get_object_or_404(CinemaHall, id=cinema_hall_id)
    movie = get_object_or_404(Movie, id=movie_id)

    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=cinema_hall,
        movie=movie
    )


def get_movies_sessions(session_date: str = None) -> QuerySet | MovieSession:
    queryset = MovieSession.objects.all()

    if session_date:
        queryset = queryset.filter(show_time__date=session_date)

    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return get_object_or_404(MovieSession, id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: str = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> None:
    movie_session = MovieSession.objects.get(id=session_id)

    if show_time:
        movie_session.show_time = show_time
    if movie_id:
        movie_session.movie = get_object_or_404(Movie, id=movie_id)
    if cinema_hall_id:
        movie_session.cinema_hall = get_object_or_404(
            CinemaHall, id=cinema_hall_id
        )

    movie_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    get_object_or_404(MovieSession, id=session_id).delete()
