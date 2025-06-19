from datetime import datetime
from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movies_sessions(session_date: str = None) -> QuerySet:
    if session_date:
        date_object = datetime.strptime(session_date, "%Y-%m-%d").date()
        return MovieSession.objects.filter(show_time__date=date_object)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> MovieSession:
    up_movie = MovieSession.objects.filter(id=session_id)
    updated_fields = {}

    if show_time:
        updated_fields["show_time"] = show_time
    if movie_id:
        updated_fields["movie_id"] = movie_id
    if cinema_hall_id:
        updated_fields["cinema_hall_id"] = cinema_hall_id

    if updated_fields:
        up_movie.update(**updated_fields)
    return up_movie


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
