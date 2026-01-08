from datetime import datetime

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> MovieSession:
    return MovieSession.objects.create(show_time=movie_show_time,
                                       movie_id=movie_id,
                                       cinema_hall_id=cinema_hall_id)


def get_movies_sessions(session_date: datetime = None) -> QuerySet:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)

    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        cinema_hall_id: int = None,
        movie_id: int = None
) -> MovieSession:
    movie_session_update = MovieSession.objects.get(id=session_id)

    if show_time:
        movie_session_update.show_time = show_time

    if movie_id:
        movie_session_update.movie_id = movie_id

    if cinema_hall_id:
        movie_session_update.cinema_hall_id = cinema_hall_id

    movie_session_update.save()

    return movie_session_update


def delete_movie_session_by_id(session_id: int) -> MovieSession:
    return get_movie_session_by_id(session_id).delete()
