from typing import List, Optional
from django.db.models import DateTimeField
from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(movie_show_time: DateTimeField,
                         movie_id: int,
                         cinema_hall_id: int) -> None:
    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)

    MovieSession.objects.create(show_time=movie_show_time,
                                movie=movie,
                                cinema_hall=cinema_hall)


def get_movies_sessions(
        session_date: Optional[DateTimeField] = None
) -> List[MovieSession]:
    if session_date is None:
        return (MovieSession.objects.all().
                values_list("show_time", "movie__title"))
    else:
        return (MovieSession.objects.
                filter(show_time__date=session_date).
                values_list("show_time", "movie__title"))


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: Optional[DateTimeField] = None,
                         movie_id: Optional[int] = None,
                         cinema_hall_id: Optional[int] = None) -> None:
    session = MovieSession.objects.get(id=session_id)
    if show_time:
        session.show_time = show_time

    if movie_id:
        session.movie = Movie.objects.get(id=movie_id)

    if cinema_hall_id:
        session.cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)

    session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    session = MovieSession.objects.get(id=session_id)
    session.delete()
