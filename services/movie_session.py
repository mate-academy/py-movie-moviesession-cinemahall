from django.db.models import QuerySet
from datetime import datetime
from db.models import Movie, CinemaHall, MovieSession


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int, cinema_hall_id: int
) -> MovieSession:

    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movies_sessions(session_date: str = None) -> QuerySet:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> MovieSession:
    session_to_update = MovieSession.objects.get(id=session_id)
    if show_time:
        session_to_update.show_time = show_time
    if movie_id:
        session_to_update.movie = Movie.objects.get(id=movie_id)
    if cinema_hall_id:
        session_to_update.cinema_hall = CinemaHall.objects.get(
            id=cinema_hall_id
        )
    session_to_update.save()
    return session_to_update


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
