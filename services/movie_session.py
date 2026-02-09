from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(movie_show_time: str,
                         movie_id: int,
                         cinema_hall_id: int) -> None:
    MovieSession.objects.create(show_time=movie_show_time,
                                movie_id=movie_id,
                                cinema_hall_id=cinema_hall_id)


def get_movies_sessions(session_date: str | None = None) -> QuerySet:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: str | None = None,
                         movie_id: int | None = None,
                         cinema_hall_id: int | None = None) -> None:
    MovieSession.objects.get(id=session_id)
    dict1 = {}
    if show_time is not None:
        dict1["show_time"] = show_time
    if movie_id is not None:
        dict1["movie_id"] = movie_id
    if cinema_hall_id is not None:
        dict1["cinema_hall_id"] = cinema_hall_id
    if dict1:
        MovieSession.objects.filter(id=session_id).update(**dict1)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
