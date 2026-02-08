from datetime import datetime

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movies_sessions(session_date: str = None) -> QuerySet:
    movie_sessions = MovieSession.objects.all()
    if session_date:
        movie_sessions = movie_sessions.filter(show_time__date=session_date)

    return movie_sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession | None:
    try:
        return MovieSession.objects.get(id=movie_session_id)
    except MovieSession.DoesNotExist:
        print(f"Movie Session with id {movie_session_id} does not exist")


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    try:
        session = MovieSession.objects.get(id=session_id)
    except MovieSession.DoesNotExist:
        print(f"Movie Session with id {session_id} does not exist")
        return
    else:
        if show_time:
            session.show_time = show_time
        if movie_id:
            session.movie_id = movie_id
        if cinema_hall_id:
            session.cinema_hall_id = cinema_hall_id

    session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    try:
        MovieSession.objects.get(id=session_id).delete()
    except MovieSession.DoesNotExist:
        print(f"Movie Session with id {session_id} does not exist")
