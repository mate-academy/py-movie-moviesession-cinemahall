from datetime import datetime

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    MovieSession.objects.create(
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id,
        show_time=movie_show_time
    )


def get_movies_sessions(session_date: str = None) -> QuerySet | MovieSession:
    if session_date:
        datetime_obj = datetime.strptime(session_date, "%Y-%m-%d")
        return MovieSession.objects.filter(
            show_time__day=datetime_obj.day,
            show_time__month=datetime_obj.month,
            show_time__year=datetime_obj.year
        )
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None,
) -> None:
    sessions = MovieSession.objects.filter(id=session_id)
    if show_time:
        sessions.update(show_time=show_time)
    if movie_id:
        sessions.update(movie_id=movie_id)
    if cinema_hall_id:
        sessions.update(cinema_hall_id=cinema_hall_id)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
