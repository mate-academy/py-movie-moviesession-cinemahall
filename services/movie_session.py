from datetime import datetime
from typing import Optional

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int
                         ) -> MovieSession:
    return MovieSession.objects.create(movie_show_time=movie_show_time,
                                       movie_id=movie_id,
                                       cinema_hall_id=cinema_hall_id)


def get_movies_sessions(session_date: Optional[str] = None) -> QuerySet[MovieSession]:
    if session_date:
        # конвертуємо рядок у datetime.date
        try:
            date_obj = datetime.strptime(session_date, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("session_date must be in 'YYYY-MM-DD' format")

        return MovieSession.objects.filter(show_time__date=date_obj)

    return MovieSession.objects.all()


def get_movie_session_by_id(session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=session_id)


def update_movie_session(session_id: int,
                         show_time: Optional[datetime] = None,
                         movie_id: Optional[int] = None,
                         cinema_hall_id: Optional[int] = None
                         ) -> None:
    update_fields = {}

    if show_time is not None:
        update_fields["show_time"] = show_time
    if movie_id is not None:
        update_fields["movie_id"] = movie_id
    if cinema_hall_id is not None:
        update_fields["cinema_hall_id"] = cinema_hall_id

    if update_fields:
        MovieSession.objects.filter(id=session_id).update(**update_fields)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
