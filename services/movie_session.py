from django.db.models import QuerySet
from datetime import datetime

from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id,
    )


def get_movies_sessions(session_date: str = None) -> QuerySet[MovieSession]:
    if session_date:
        return MovieSession.objects.filter(
            show_time__date=datetime.strptime(session_date, "%Y-%m-%d")
        )

    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    try:
        return MovieSession.objects.get(id=movie_session_id)
    except MovieSession.DoesNotExist:
        pass


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None,
) -> None:
    movie_session = None
    try:
        movie_session = MovieSession.objects.get(id=session_id)
    except MovieSession.DoesNotExist:
        pass
    if show_time:
        movie_session.show_time = show_time
    if movie_id:
        movie_session.movie_id = movie_id
    if cinema_hall_id:
        movie_session.cinema_hall_id = cinema_hall_id
    movie_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    try:
        MovieSession.objects.get(id=session_id).delete()
    except MovieSession.DoesNotExist:
        pass
