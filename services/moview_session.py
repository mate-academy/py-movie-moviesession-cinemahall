from datetime import datetime
from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int
) -> MovieSession:
    MovieSession.objects.create(show_time=movie_show_time, id=movie_id)
    return MovieSession.objects.get(id=movie_id)


def get_movie_sessions(session_date: str = None) -> [MovieSession]:
    movies = MovieSession.objects.all()
    if session_date is None:
        movies = movies.filter(session_date=session_date)
    return [movies]


def update_movie_session(
        session_id: int,
        show_time: datetime,
        cinema_hall_id: int = None
) -> None:
    movie_session = MovieSession.objects.get(id=session_id)
    movie_session.update(show_time=show_time)
    if cinema_hall_id is not None:
        movie_session.update(cinema_hall=cinema_hall_id)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
