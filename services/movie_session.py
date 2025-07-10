from datetime import datetime
from typing import Optional

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> MovieSession:
    return MovieSession.objects.get_or_create(show_time=movie_show_time,
                                              cinema_hall_id=cinema_hall_id,
                                              movie_id=movie_id)[0]


def get_movies_sessions(session_date: Optional[str] = None) -> (QuerySet
                                                                [MovieSession]):

    if session_date is not None:
        date = datetime.strptime(session_date, "%Y-%m-%d")
        print(date.strftime("%Y-%m-%d"))
        return MovieSession.objects.filter(show_time__date=date.date())

    return MovieSession.objects.all()


def get_movie_session_by_id(movie_id: int) -> QuerySet[MovieSession]:
    return MovieSession.objects.get(id=movie_id)


def update_movie_session(session_id: int,
                         show_time: Optional[datetime] = None,
                         movie_id: Optional[int] = None,
                         cinema_hall_id: Optional[int] = None) -> None:

    update_fields = dict()

    if show_time is not None:
        update_fields["show_time"] = show_time
    if movie_id is not None:
        update_fields["movie_id"] = movie_id
    if cinema_hall_id is not None:
        update_fields["cinema_hall_id"] = cinema_hall_id

    if update_fields:
        MovieSession.objects.filter(id=session_id).update(**update_fields)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
