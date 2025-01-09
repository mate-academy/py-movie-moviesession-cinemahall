from datetime import datetime

from db.models import MovieSession
from django.db.models import QuerySet


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id,
    )


def get_movies_sessions(
        session_date: str = None
) -> QuerySet[MovieSession]:
    if session_date:
        return MovieSession.objects.filter(
            show_time__date=datetime.strptime(
                session_date, "%Y-%m-%d"
            ).date())
    return MovieSession.objects.all()


def get_movie_session_by_id(
        movie_session_id: int
) -> MovieSession:
    return MovieSession.objects.filter(
        id=movie_session_id
    ).first()


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None,
) -> None:
    if show_time:
        MovieSession.objects.filter(id=session_id).update(
            show_time=show_time,
        )

    if movie_id:
        MovieSession.objects.filter(id=session_id).update(
            movie_id=movie_id
        )

    if cinema_hall_id:
        MovieSession.objects.filter(id=session_id).update(
            cinema_hall_id=cinema_hall_id
        )


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
