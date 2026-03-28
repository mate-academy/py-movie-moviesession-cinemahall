from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(movie_id: int,
                         cinema_hall_id: int,
                         movie_show_time: int) -> None:
    MovieSession.objects.create(movie_id=movie_id,
                                cinema_hall_id=cinema_hall_id,
                                cinema_id=movie_show_time)


def get_movies_sessions(session_date: str) -> QuerySet:
    if session_date:
        return MovieSession.objects.filter(session_date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(movie_session_id: int,
                         show_time: int = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> None:
    movie_session = MovieSession.objects.get(id=movie_session_id)

    if show_time is not None:
        movie_session.cinema_id = show_time
    if movie_id is not None:
        movie_session.movie_id = movie_id
    if cinema_hall_id is not None:
        movie_session.cinema_hall_id = cinema_hall_id

    movie_session.save()


def delete_movie_session_by_id(movie_session_id: int) -> None:
    MovieSession.objects.get(id=movie_session_id).delete()
