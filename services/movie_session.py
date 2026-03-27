import init_django_orm # noqa F401
from db.models import MovieSession


def create_movie_session(movie_show_time, movie_id, cinema_hall_id):
    new_movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )
    return new_movie_session


def get_movies_sessions(session_date=None):
    sessions = MovieSession.objects.all()
    if session_date:
        sessions = sessions.filter(show_time__date=session_date)
    return sessions


def get_movie_session_by_id(movie_session_id):
    return MovieSession.objects.filter(id=movie_session_id).first()


def update_movie_session(session_id,
                         show_time=None,
                         movie_id=None,
                         cinema_hall_id=None):
    session_to_update = MovieSession.objects.filter(id=session_id)
    if show_time:
        session_to_update.update(show_time=show_time)
    if movie_id:
        session_to_update.update(movie_id=movie_id)
    if cinema_hall_id:
        session_to_update.update(cinema_hall_id=cinema_hall_id)
    return session_to_update


def delete_movie_session_by_id(session_id):
    session_to_delete = MovieSession.objects.filter(id=session_id)
    return session_to_delete.delete()
