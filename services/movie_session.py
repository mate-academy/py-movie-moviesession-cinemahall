from datetime import datetime

from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movies_sessions(session_date: str = None) -> MovieSession:
    queryset = MovieSession.objects.all()

    if session_date is not None:
        date = datetime.strptime(session_date, "%Y-%m-%d")
        queryset = queryset.filter(show_time__date=date)

    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    queryset = MovieSession.objects.filter(id=session_id)

    if show_time is not None:
        queryset.update(show_time=show_time)

    if movie_id is not None:
        queryset.update(movie=movie_id)

    if cinema_hall_id is not None:
        queryset.update(cinema_hall=cinema_hall_id)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
