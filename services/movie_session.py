from datetime import datetime

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int,
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(session_date: str = None) -> QuerySet[MovieSession]:
    if session_date:
        return MovieSession.objects.filter(
            show_time__date=datetime.strptime(session_date, "%Y-%m-%d"))

    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = 0,
        cinema_hall_id: int = 0,
) -> None:
    update_fields = {}

    if show_time:
        update_fields["show_time"] = show_time

    if movie_id != 0:
        update_fields["movie_id"] = movie_id

    if cinema_hall_id != 0:
        update_fields["cinema_hall_id"] = cinema_hall_id

    if update_fields:
        MovieSession.objects.filter(id=session_id).update(**update_fields)


def delete_movie_session_by_id(movie_session_id: int) -> None:
    get_movie_session_by_id(movie_session_id).delete()
