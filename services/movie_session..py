from django.db.models import QuerySet
import datetime
from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime.datetime,
        movie_id: int,
        cinema_hall_id: id
) -> QuerySet[MovieSession]:
    movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )
    return movie_session


def get_movies_sessions(session_date: str = None) -> QuerySet[MovieSession]:
    movie = MovieSession.objects.all()
    if session_date:
        movie = movie.filter(
            show_time__date=session_date
        )
    return movie


def get_movie_session_by_id(movie_id: int) -> QuerySet[MovieSession]:
    return MovieSession.objects.get(id=movie_id)


def update_movie_session(
        session_id: int,
        show_time: datetime.datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
        ) -> None:
    movie_session = MovieSession.objects.get(id=session_id)
    if show_time:
        movie_session.show_time = show_time
    if movie_id:
        movie_session.movie_id = movie_id
    if cinema_hall_id:
        movie_session.cinema_hall_id = cinema_hall_id
    movie_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
