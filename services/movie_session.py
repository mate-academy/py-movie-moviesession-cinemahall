import datetime

from db.models import MovieSession


def create_movie_session(movie_show_time: datetime,
                         movie_id: int, cinema_hall_id: int):
    result = MovieSession.objects.create(show_time=movie_show_time,
                                         movie_id=movie_id,
                                         cinema_hall_id=cinema_hall_id)
    return result


def get_movies_sessions(session_date: str = None):
    result = MovieSession.objects.all()
    if session_date:
        result = result.filter(show_time__date=session_date)

    return result


def get_movie_session_by_id(movie_session_id: int):
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int, show_time: datetime = None,
                         movie_id: int = None, cinema_hall_id: int = None):
    result = MovieSession.objects.filter(id=session_id)

    if show_time:
        result.update(show_time=show_time)
    if movie_id:
        result.update(movie_id=movie_id)
    if cinema_hall_id:
        result.update(cinema_hall_id=cinema_hall_id)

    return result


def delete_movie_session_by_id(session_id: int):
    MovieSession.objects.filter(id=session_id).delete()
