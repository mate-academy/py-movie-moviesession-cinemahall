from db.models import MovieSession
from django.db.models.query import QuerySet


def create_movie_session(movie_show_time: str,
                         movie_id: int,
                         cinema_hall_id: int) -> None:
    MovieSession.objects.create(show_time=movie_show_time,
                                movie_id=movie_id,
                                cinema_hall_id=cinema_hall_id)


def get_movies_sessions(session_date: str = None) -> QuerySet:
    if session_date is not None:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> QuerySet:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: str = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> None:
    movie_session_object = MovieSession.objects.get(id=session_id)
    if show_time is None:
        show_time = movie_session_object.show_time
    if movie_id is None:
        movie_id = movie_session_object.movie_id
    if cinema_hall_id is None:
        cinema_hall_id = movie_session_object.cinema_hall_id
    MovieSession.objects.filter(id=session_id).update(
        show_time=show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
