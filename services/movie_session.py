from django.db.models import QuerySet
from db.models import MovieSession, Movie
from datetime import datetime


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> QuerySet[Movie]:

    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def get_movies_sessions(session_date: str = None) -> QuerySet:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        cinema_hall_id: int = None,
        movie_id: int = None
) -> MovieSession:
    movie_s = MovieSession.objects.get(id=session_id)

    if show_time:
        movie_s.show_time = show_time
    if cinema_hall_id:
        movie_s.cinema_hall_id = cinema_hall_id
    if movie_id:
        movie_s.movie_id = movie_id

    movie_s.save()
    return movie_s


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
