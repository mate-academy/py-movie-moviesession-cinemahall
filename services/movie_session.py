from django.db.models import QuerySet

import init_django_orm  # noqa : F401

from db.models import MovieSession


def create_movie_session(movie_show_time: str,
                         movie_id: int,
                         cinema_hall_id: int) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movies_sessions(session_date: str = None) -> QuerySet:
    movie_sessions = MovieSession.objects.all()
    if session_date:
        year, month, day = session_date.split("-")
        movie_sessions = MovieSession.objects.filter(show_time__year=year,
                                                     show_time__month=month,
                                                     show_time__day=day)
        if not movie_sessions:
            return MovieSession.objects.all()

    return movie_sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    movie_session = MovieSession.objects.get(id=movie_session_id)
    return movie_session


def update_movie_session(session_id: int,
                         show_time: str = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> None:
    movie_session = MovieSession.objects.get(id=session_id)

    if show_time:
        movie_session.show_time = show_time
    if movie_id:
        movie_session.movie_id = movie_id
    if cinema_hall_id:
        movie_session.cinema_hall_id = cinema_hall_id

    movie_session.save()


def delete_movie_session_by_id(session_id: int) -> MovieSession:
    movie = MovieSession.objects.get(id=session_id).delete()
    return movie
