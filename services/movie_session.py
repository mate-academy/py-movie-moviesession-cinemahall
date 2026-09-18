from db.models import MovieSession
from datetime import datetime
from django.db.models import QuerySet


def create_movie_session(
    movie_show_time: str, movie_id: int, cinema_hall_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id,
        show_time=movie_show_time
    )


def get_movies_sessions(
    session_date: str = None,
) -> QuerySet[MovieSession]:
    sessions = MovieSession.objects.all()
    if session_date:
        dt_obj = datetime.strptime(session_date, "%Y-%m-%d")
        parsed_date = dt_obj.date()
        sessions = sessions.filter(
            show_time__date=parsed_date
        )
    return sessions


def get_movie_session_by_id(
    movie_session_id: int
) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
    session_id: int,
    show_time: str = None,
    movie_id: int = None,
    cinema_hall_id: int = None,
) -> MovieSession:
    session = MovieSession.objects.get(id=session_id)
    if show_time:
        session.show_time = show_time
    if movie_id:
        session.movie_id = movie_id
    if cinema_hall_id:
        session.cinema_hall_id = cinema_hall_id
    session.save()
    return session


def delete_movie_session_by_id(session_id: int) -> None:
    session = MovieSession.objects.get(id=session_id)
    session.delete()
