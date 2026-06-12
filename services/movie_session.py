import datetime

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
    movie_show_time: datetime.datetime,
    movie_id: int,
    cinema_hall_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id,
    )


def get_movie_session_by_id(
    session_id: int
) -> MovieSession:
    return MovieSession.objects.get(id=session_id)


def get_movies_sessions(
    session_date: str | None = None,
) -> QuerySet[MovieSession]:
    if session_date is not None:
        return MovieSession.objects.filter(
            show_time__date=session_date
        )

    return MovieSession.objects.all()


def update_movie_session(
    session_id: int,
    show_time: str | datetime.datetime | None = None,
    movie_id: int | None = None,
    cinema_hall_id: int | None = None,
) -> MovieSession:
    movie_session = MovieSession.objects.get(
        id=session_id
    )

    updated_fields = []

    if show_time is not None:
        movie_session.show_time = show_time
        updated_fields.append("show_time")

    if movie_id is not None:
        movie_session.movie_id = movie_id
        updated_fields.append("movie_id")

    if cinema_hall_id is not None:
        movie_session.cinema_hall_id = cinema_hall_id
        updated_fields.append("cinema_hall_id")

    if updated_fields:
        movie_session.save(update_fields=updated_fields)

    return movie_session


def delete_movie_session_by_id(session_id: int) -> None:
    movie_session = MovieSession.objects.get(id=session_id)
    movie_session.delete()
