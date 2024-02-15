from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from db.models import MovieSession
from datetime import datetime


def create_movie_session(
    movie_show_time: datetime, movie_id: int, cinema_hall_id: int
) -> MovieSession:

    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movies_sessions(
    session_date: str = None,
) -> QuerySet[MovieSession]:
    movie_sessions = MovieSession.objects.all()

    if session_date:
        try:
            format_date = datetime.strptime(session_date, "%Y-%m-%d").date()
            movie_sessions = movie_sessions.filter(show_time__date=format_date)
        except ValueError:
            raise Exception("Incorrect format of date.")

    return movie_sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return get_object_or_404(MovieSession, id=movie_session_id)


def update_movie_session(
    session_id: int,
    show_time: datetime = None,
    movie_id: int = None,
    cinema_hall_id: int = None,
) -> MovieSession:

    movie_session = get_movie_session_by_id(session_id)

    if show_time:
        movie_session.show_time = show_time
    if movie_id:
        movie_session.movie_id = movie_id
    if cinema_hall_id:
        movie_session.cinema_hall_id = cinema_hall_id

    movie_session.save()

    return movie_session


def delete_movie_session_by_id(session_id: int) -> None:
    try:
        get_movie_session_by_id(session_id).delete()
    except MovieSession.DoesNotExist as e:
        raise e("Movie session does not exist.")
