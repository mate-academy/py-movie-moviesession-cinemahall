from datetime import datetime
from django.db.models import QuerySet
from db.models import MovieSession


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(session_date: str = None) -> QuerySet:
    movie_session = MovieSession.objects.all()
    if session_date:
        date_time = datetime.strptime(session_date, "%Y-%m-%d")
        return movie_session.filter(
            show_time__date=date_time.date()
        )
    return movie_session


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> None:
    new_movie_session = MovieSession.objects.filter()

    if show_time:
        new_movie_session.filter(id=session_id).update(show_time=show_time)

    if movie_id:
        new_movie_session.filter(id=session_id
                                 ).update(movie_id=movie_id)
    if cinema_hall_id:
        new_movie_session.filter(id=session_id
                                 ).update(cinema_hall_id=cinema_hall_id)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
