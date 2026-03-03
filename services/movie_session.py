from datetime import datetime
from django.db.models import QuerySet

from db.models import MovieSession


def get_movies_sessions(session_date: str = None) -> QuerySet:
    query_set = MovieSession.objects.all()

    if session_date:
        session_date = datetime.strptime(
            session_date, "%Y-%m-%d"
        ).date()
        return MovieSession.objects.filter(show_time__date=session_date)

    return query_set


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def update_movie_session(session_id: int,
                         show_time: datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> MovieSession:
    movie_session_to_upd = MovieSession.objects.get(id=session_id)
    if show_time:
        movie_session_to_upd.show_time = show_time
    if movie_id:
        movie_session_to_upd.movie_id = movie_id
    if cinema_hall_id:
        movie_session_to_upd.cinema_hall_id = cinema_hall_id
    movie_session_to_upd.save()

    return movie_session_to_upd


def delete_movie_session_by_id(session_id: int) -> tuple[int, dict[str, int]]:
    return MovieSession.objects.filter(id=session_id).delete()
