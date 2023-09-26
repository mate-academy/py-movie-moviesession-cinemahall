from db.models import MovieSession
from datetime import datetime, date


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )
    return movie_session


def get_movies_sessions(session_date: date = None) -> MovieSession:
    all_movie_sessions = MovieSession.objects.all()

    if session_date:
        all_movie_sessions = MovieSession.objects.filter(
            show_time__date=session_date
        )
    return all_movie_sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int = None,
                         show_time: datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> MovieSession:
    update_session = MovieSession.objects.get(
        id=session_id
    )

    if show_time:
        update_session.show_time = show_time

    if movie_id:
        update_session.movie_id = movie_id

    if cinema_hall_id:
        update_session.cinema_hall_id = cinema_hall_id

    update_session.save()

    return update_session


def delete_movie_session_by_id(session_id: int) -> MovieSession:
    return MovieSession.objects.filter(id=session_id).delete()
