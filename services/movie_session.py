from typing import Optional

from django.db.models import QuerySet

from db.models import CinemaHall, Movie, MovieSession


def create_movie_session(movie_show_time: str,
                         movie_id: int,
                         cinema_hall_id: int
                         ) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall=CinemaHall(pk=cinema_hall_id)
    )


def get_movies_sessions(
        session_date: Optional[str] = None
) -> QuerySet:
    movies_sessions = MovieSession.objects.all()
    if session_date:
        return MovieSession.objects.filter(
            show_time__date=session_date
        )
    return movies_sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(pk=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: Optional[str] = None,
                         movie_id: Optional[int] = None,
                         cinema_hall_id: Optional[int] = None
                         ) -> None:
    movie_session = get_movie_session_by_id(session_id)

    if show_time:
        movie_session.show_time = show_time

    if movie_id:
        movie_session.movie = Movie(pk=movie_id)

    if cinema_hall_id:
        movie_session.cinema_hall = CinemaHall(pk=cinema_hall_id)

    movie_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    get_movie_session_by_id(session_id).delete()
