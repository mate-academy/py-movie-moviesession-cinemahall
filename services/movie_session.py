from typing import List

from django.http import Http404
from django.shortcuts import get_object_or_404

from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int,
) -> None:
    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)

    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=cinema_hall,
        movie=movie
    )


def get_movies_sessions(session_date: str = None) -> List[MovieSession]:
    if session_date is None:
        return MovieSession.objects.all()
    return MovieSession.objects.filter(show_time__date=session_date)


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    movie_session = get_movie_session_by_id(session_id)

    try:
        movie = get_object_or_404(Movie, pk=movie_id)
        movie_session.movie = movie
    except Http404:
        pass

    try:
        cinema_hall = get_object_or_404(CinemaHall, pk=cinema_hall_id)
        movie_session.cinema_hall = cinema_hall
    except Http404:
        pass

    if show_time is not None:
        movie_session.show_time = show_time
    movie_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
