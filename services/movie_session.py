import datetime

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(
        session_date: datetime.datetime | None = None
) -> QuerySet[MovieSession]:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_id)


def update_movie_session(
    session_id: int | None = None,
    show_time: datetime.datetime | None = None,
    movie_id: int | None = None,
    cinema_hall_id: int | None = None
) -> None:
    if show_time or movie_id or cinema_hall_id:
        update_kwargs = {}
        for key, value in locals().items():
            if key != "session_id" and value and hasattr(MovieSession, key):
                update_kwargs[key] = value
        MovieSession.objects.filter(id=session_id).update(**update_kwargs)


def delete_movie_session_by_id(_id: int) -> None:
    MovieSession.objects.filter(id=_id).delete()
