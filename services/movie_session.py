from datetime import datetime

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int,
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movies_sessions(session_date: str = None) -> QuerySet:
    movies_sessions = MovieSession.objects.all()
    if session_date:
        session_date = datetime.strptime(session_date, "%Y-%m-%d").date()
        movies_sessions = movies_sessions.filter(show_time__date=session_date)
    return movies_sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> MovieSession:
    updated_movie_session = MovieSession.objects.get(id=session_id)
    if show_time:
        updated_movie_session.show_time = show_time
    if movie_id:
        updated_movie_session.movie_id = movie_id
    if cinema_hall_id:
        updated_movie_session.cinema_hall_id = cinema_hall_id
    updated_movie_session.save()
    return updated_movie_session


def delete_movie_session_by_id(session_id: int) -> tuple:
    return get_movie_session_by_id(session_id).delete()
