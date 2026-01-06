from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    new_session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )
    return new_session


def get_movies_sessions(session_date: str = None) -> QuerySet[MovieSession]:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession | None:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    updates = {}
    if show_time is not None:
        updates["show_time"] = show_time
    if movie_id is not None:
        updates["movie_id"] = movie_id
    if cinema_hall_id is not None:
        updates["cinema_hall_id"] = cinema_hall_id

    (MovieSession.objects.filter(id=session_id)
     .update(**updates))


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
