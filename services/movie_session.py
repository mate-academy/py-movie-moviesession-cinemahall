from datetime import datetime

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> MovieSession:
    return MovieSession.objects.create(
        movie_id=movie_id,
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
    )


def get_movies_sessions(session_date: str = None) -> QuerySet[MovieSession] | MovieSession:
    sessions = MovieSession.objects.all()
    if session_date:
        try:
            date_obj = datetime.strptime(session_date, "%Y-%m-%d").date()
            sessions = sessions.filter(show_time__date=date_obj)
        except ValueError:
            raise ValueError("Incorrect date format")
    return sessions


def get_movie_session_by_id(movie_session_id: int ) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> MovieSession:
    movie_session = get_movie_session_by_id(session_id)
    if show_time:
        movie_session.show_time = show_time
    if movie_id:
        movie_session.movie_id = movie_id
    if cinema_hall_id:
        movie_session.cinema_hall_id = cinema_hall_id
    movie_session.save()

    return movie_session


def delete_movie_session_by_id(session_id: int) -> bool:
    deleted_count, _ = MovieSession.objects.filter(id=session_id).delete()
    return deleted_count > 0
