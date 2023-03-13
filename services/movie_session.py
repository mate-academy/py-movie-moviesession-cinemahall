import datetime

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime.datetime,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movies_sessions(session_date: str = None) -> QuerySet:
    movie_session = MovieSession.objects.all()

    if session_date:
        year, month, day = session_date.split("-")
        movie_session = movie_session.filter(
            show_time__date=datetime.date(
                year=int(year),
                month=int(month),
                day=int(day)
            )
        )

    return movie_session


def get_movie_session_by_id(
        movie_session_id: int
) -> MovieSession:
    return MovieSession.objects.get(
        id=movie_session_id
    )


def update_movie_session(
        session_id: int,
        show_time: datetime.datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    new_movie_session = MovieSession.objects.filter(id=session_id)

    if show_time:
        new_movie_session.update(show_time=show_time)

    if movie_id:
        new_movie_session.update(movie_id=movie_id)

    if cinema_hall_id:
        new_movie_session.update(cinema_hall_id=cinema_hall_id)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
