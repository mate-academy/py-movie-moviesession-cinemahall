from datetime import datetime
from typing import Optional, Union

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int,
) -> MovieSession:
    if isinstance(movie_show_time, str):
        try:
            movie_show_time = (datetime.strptime
                               (movie_show_time,
                                "%Y-%m-%d %H:%M:%S")
                               )
        except ValueError:
            raise TypeError("Movie show time must be in format"
                            " YYYY-MM-DD HH:MM:SS")
    elif not isinstance(movie_show_time, datetime):
        raise TypeError("movie_show_time must be str or datetime")

    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movies_sessions(session_date: Optional[str] = None
                        ) -> QuerySet[MovieSession]:
    if session_date is None:
        return MovieSession.objects.all()
    else:
        return MovieSession.objects.filter(show_time__date=session_date)


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: Optional[Union[datetime, str]] = None,
        movie_id: Optional[int] = None,
        cinema_hall_id: Optional[int] = None,
) -> MovieSession:

    session = MovieSession.objects.get(id=session_id)

    update_fields = []

    if show_time is not None:
        if isinstance(show_time, str):
            try:
                show_time = datetime.strptime(
                    show_time,
                    "%Y-%m-%d %H:%M:%S"
                )
            except ValueError:
                raise TypeError("show_time must be format %Y-%m-%d %H:%M:%S")
        session.show_time = show_time
        update_fields.append("show_time")

    if movie_id is not None:
        session.movie_id = movie_id
        update_fields.append("movie_id")

    if cinema_hall_id is not None:
        session.cinema_hall_id = cinema_hall_id
        update_fields.append("cinema_hall_id")

    if update_fields:
        session.save(update_fields=update_fields)

    return session


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
    return None
