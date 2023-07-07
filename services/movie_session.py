from datetime import datetime, timedelta
from typing import Optional

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(
        session_date: Optional[str] = None
) -> QuerySet[MovieSession]:
    if not session_date:
        return MovieSession.objects.all()
    start_time = datetime.strptime(session_date, "%Y-%m-%d")
    end_time = start_time + timedelta(days=1)
    return MovieSession.objects.filter(
        show_time__range=[start_time, end_time]
    )


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: Optional[datetime] = None,
        movie_id: Optional[int] = None,
        cinema_hall_id: Optional[int] = None
) -> None:
    updated_movie_session = get_movie_session_by_id(session_id)
    if show_time:
        updated_movie_session.show_time = show_time
    if movie_id:
        updated_movie_session.movie_id = movie_id
    if cinema_hall_id:
        updated_movie_session.cinema_hall_id = cinema_hall_id
    updated_movie_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    get_movie_session_by_id(session_id).delete()
