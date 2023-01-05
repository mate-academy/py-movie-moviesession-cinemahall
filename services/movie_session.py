from datetime import datetime
from django.db.models import QuerySet
from db.models import CinemaHall, Movie
from db.models import MovieSession


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> None:

    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=CinemaHall.objects.get(id=cinema_hall_id),
        movie=Movie.objects.get(id=movie_id)
    )


def get_movies_sessions(session_date: str = None) -> QuerySet:
    queryset = MovieSession.objects.all()

    if session_date:
        converted_session_date = datetime.strptime(session_date, "%Y-%m-%d")
        queryset = queryset.filter(
            show_time__date=converted_session_date
        )

    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:

    movie_session = get_movie_session_by_id(session_id)

    MovieSession.objects.filter(id=session_id).update(
        show_time=show_time if show_time is not None
        else movie_session.show_time,

        movie=movie_id if movie_id is not None
        else movie_session.movie,

        cinema_hall=cinema_hall_id if cinema_hall_id is not None
        else movie_session.cinema_hall
    )


def delete_movie_session_by_id(session_id: int) -> None:
    get_movie_session_by_id(session_id).delete()
