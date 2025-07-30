from datetime import datetime

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movies_sessions(session_date: str = None) -> QuerySet[MovieSession]:
    if session_date:
        session_date = datetime.strptime(session_date, "%Y-%m-%d")
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> MovieSession:
    query = MovieSession.objects.filter(id=session_id)

    if show_time:
        query.update(show_time=show_time)
    if movie_id:
        query.update(movie_id=movie_id)
    if cinema_hall_id:
        query.update(cinema_hall_id=cinema_hall_id)
    return MovieSession.objects.get(id=session_id)


def delete_movie_session_by_id(session_id: int) -> bool:
    deleted_count, _ = MovieSession.objects.get(id=session_id).delete()
    return deleted_count > 0
