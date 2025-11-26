from datetime import datetime

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(movie_show_time: datetime, movie_id: int,
                         cinema_hall_id: int) -> None:
    MovieSession.objects.create(show_time=movie_show_time,
                                movie_id=movie_id,
                                cinema_hall_id=cinema_hall_id)


def get_movies_sessions(session_date:str = None) -> QuerySet:
     movie_sessions=MovieSession.objects.all()
     if session_date:
        movie_sessions =MovieSession.objects.filter(show_time__date=session_date)
     return movie_sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession | None:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int, **kwargs) -> None:
    allowed_fields = {"show_time", "movie_id", "cinema_hall_id"}
    update_data = {k: v for k, v in kwargs.items() if k in allowed_fields}
    if update_data:
        MovieSession.objects.filter(id=session_id).update(**update_data)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
