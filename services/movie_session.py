import datetime
from db.models import MovieSession


def create_movie_session(
    movie_id: int, movie_show_time: datetime.datetime, cinema_hall_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        movie_id=movie_id,
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
    )


def get_movies_sessions(
    session_date: datetime.date | None = None,
) -> MovieSession:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=session_id)


def update_movie_session(
    session_id: int,
    show_time: datetime.datetime | None = None,
    movie_id: int | None = None,
    cinema_hall_id: int | None = None,
) -> MovieSession:
    session = MovieSession.objects.get(id=session_id)
    if show_time:
        session.show_time = show_time
    if movie_id:
        session.movie_id = movie_id
    if cinema_hall_id:
        session.cinema_hall_id = cinema_hall_id
    session.save()
    return session


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
