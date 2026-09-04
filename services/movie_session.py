from django.db.models.query import QuerySet


from datetime import date
from db.models import MovieSession


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    new_movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )
    return new_movie_session


def get_movies_sessions(
        session_date: date | None = None
) -> QuerySet[MovieSession]:
    if session_date is not None:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: str | None = None,
        movie_id: int | None = None,
        cinema_hall_id: int | None = None
) -> MovieSession:
    updates = {}
    if show_time:
        updates["show_time"] = show_time
    if movie_id:
        updates["movie_id"] = movie_id
    if cinema_hall_id:
        updates["cinema_hall_id"] = cinema_hall_id
    updated_movie_session = MovieSession.objects.update_or_create(
        id=session_id,
        defaults=updates
    )[0]
    return updated_movie_session


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
