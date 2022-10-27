from django.db.models import DateTimeField, QuerySet

from db.models import MovieSession


def create_movie_session(movie_show_time: int,
                         movie_id: int,
                         cinema_hall_id: int) -> MovieSession:
    return MovieSession.objects.create(show_time=movie_show_time,
                                       cinema_hall_id=cinema_hall_id,
                                       movie_id=movie_id)


def get_movies_sessions(session_date: DateTimeField = None) -> QuerySet:
    sessions = MovieSession.objects.all()
    if session_date:
        sessions = sessions.filter(show_time__date=session_date)
    return sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: DateTimeField = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> MovieSession:
    update_session = MovieSession.objects.get(id=session_id)
    if show_time:
        update_session.show_time = show_time
    if movie_id:
        update_session.movie_id = movie_id
    if cinema_hall_id:
        update_session.cinema_hall_id = cinema_hall_id
    update_session.save()
    return update_session


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
