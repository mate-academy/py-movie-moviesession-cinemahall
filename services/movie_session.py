from datetime import datetime
from db.models import MovieSession


def create_movie_session(
    movie_id: int,
    cinema_hall_id: int,
    movie_show_time: datetime
) -> MovieSession:
    return MovieSession.objects.create(
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id,
        show_time=movie_show_time
    )


def get_movies_sessions(
    session_date: datetime = None
) -> list:
    if session_date:
        return MovieSession.objects.filter(
            show_time__date=session_date.date()
        )
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
    session_id: int,
    show_time: datetime = None,
    movie_id: int = None,
    cinema_hall_id: int = None
) -> MovieSession:
    session = MovieSession.objects.get(id=session_id)
    if show_time is not None:
        session.show_time = show_time
    if movie_id is not None:
        session.movie_id = movie_id
    if cinema_hall_id is not None:
        session.cinema_hall_id = cinema_hall_id
    session.save()
    return session


def delete_movie_session_by_id(
    session_id: int,
    session_date: datetime = None
) -> None:
    queryset = MovieSession.objects.filter(id=session_id)
    if session_date is not None:
        queryset = queryset.filter(show_time__date=session_date.date())
    queryset.delete()
