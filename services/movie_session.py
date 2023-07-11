from datetime import datetime
from django.db.models import QuerySet
from db.models import CinemaHall, Movie, MovieSession


def create_movie_session(
    movie_show_time: datetime,
    movie_id: int,
    cinema_hall_id: int
) -> MovieSession | None:
    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie=movie,
        cinema_hall=cinema_hall
    )


def get_movies_sessions(session_date: str = None) -> QuerySet[MovieSession]:
    if session_date:
        return MovieSession.objects.select_related("movie").filter(
            show_time__date=session_date
        )
    return MovieSession.objects.select_related("movie").all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession | None:
    try:
        return MovieSession.objects.get(id=movie_session_id)
    except MovieSession.DoesNotExist:
        return None


def update_movie_session(
    session_id: int,
    show_time: datetime = None,
    movie_id: int = None,
    cinema_hall_id: int = None
) -> None:
    try:
        session = MovieSession.objects.get(id=session_id)
    except MovieSession.DoesNotExist:
        return
    if show_time:
        session.show_time = show_time
    if movie_id:
        session.movie_id = movie_id
    if cinema_hall_id:
        session.cinema_hall_id = cinema_hall_id
    session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
