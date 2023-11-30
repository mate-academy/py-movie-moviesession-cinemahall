from datetime import datetime

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(movie_show_time: int,
                         movie_id: int,
                         cinema_hall_id: int) -> MovieSession:
    return MovieSession.objects.create(show_time=movie_show_time,
                                       movie_id=movie_id,
                                       cinema_hall_id=cinema_hall_id)


def get_movies_sessions(
        session_date: str | None = None) -> QuerySet[MovieSession]:
    movie_session = MovieSession.objects.all()

    if session_date is not None:
        date = datetime.strptime(session_date, "%Y-%m-%d").date()
        movie_session = MovieSession.objects.filter(show_time__date=date)

    return movie_session


def get_movie_session_by_id(movie_session_id: int) -> int:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: int | None = None,
                         movie_id: int | None = None,
                         cinema_hall_id: int | None = None) -> None:
    movie_session = MovieSession.objects.get(id=session_id)

    if show_time:
        movie_session.show_time = show_time

    if movie_id:
        movie_session.movie_id = movie_id

    if cinema_hall_id:
        movie_session.cinema_hall_id = cinema_hall_id

    movie_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    session = get_movie_session_by_id(session_id)
    session.delete()
