from db.models import MovieSession
from datetime import date
from django.db.models import QuerySet


def create_movie_session(
        movie_show_time: date,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id,
    )


def get_movies_sessions(session_date: str = None) -> QuerySet[MovieSession]:
    ms = MovieSession.objects.all()

    if session_date:
        convert = tuple([int(i) for i in session_date.split("-")])
        ms = ms.filter(show_time__date=date(*convert))

    return ms


def get_movie_session_by_id(movie_id: int) -> MovieSession | None:
    return MovieSession.objects.get(id=movie_id)


def update_movie_session(
        session_id: int,
        show_time: date = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    ms = get_movie_session_by_id(session_id)

    if show_time:
        ms.show_time = show_time

    if movie_id:
        ms.movie_id = movie_id

    if cinema_hall_id:
        ms.cinema_hall_id = cinema_hall_id

    ms.save()


def delete_movie_session_by_id(session_id: int) -> None:
    ms = get_movie_session_by_id(session_id)
    ms.delete()
