from datetime import datetime
from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int
) -> MovieSession:
    MovieSession.objects.create(show_time=movie_show_time, movie_id=movie_id)
    return MovieSession.objects.get(id=movie_id)


def get_movie_sessions(session_date: str = None) -> [MovieSession]:
    movies = MovieSession.objects.all()
    if session_date is not None:
        movies = movies.filter(show_time__date=session_date)
    return list(movies)


def update_movie_session(
        session_id: int,
        show_time: datetime,
        cinema_hall_id: int = None
) -> None:
    movie_session = MovieSession.objects.get(id=session_id)
    movie_session.show_time = show_time
    if cinema_hall_id is not None:
        movie_session.cinema_hall= cinema_hall_id
    movie_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
