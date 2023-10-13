import init_django_orm  # noqa: F401
from django.db.models import QuerySet
from django.core.exceptions import ObjectDoesNotExist
from db.models import MovieSession
from datetime import datetime


def create_movie_session(
    movie_show_time: datetime, movie_id: int, cinema_hall_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id,
    )


def get_movies_sessions(session_date: str = None) -> QuerySet[MovieSession]:
    movie_sessions = MovieSession.objects.all()
    if session_date:
        try:
            date_obj = datetime.strptime(session_date, "%Y-%m-%d")
            movie_sessions = movie_sessions.filter(show_time__date=date_obj)
        except ValueError:
            print("You provided incorrect data")
            print("Please, provide data in format 'year-month-day'")
            return QuerySet()
    return movie_sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
    session_id: int,
    show_time: datetime = None,
    movie_id: int = None,
    cinema_hall_id: int = None,
) -> None:

    try:
        movie_session = get_movie_session_by_id(session_id)
    except ObjectDoesNotExist:
        print("You provided incorrect ID")
        return

    if show_time is not None:
        movie_session.show_time = show_time

    if movie_id is not None:
        movie_session.movie_id = movie_id

    if cinema_hall_id is not None:
        movie_session.cinema_hall_id = cinema_hall_id

    movie_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    movie_session = get_movie_session_by_id(session_id)
    movie_session.delete()
