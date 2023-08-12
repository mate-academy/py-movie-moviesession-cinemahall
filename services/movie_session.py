from db.models import MovieSession
from datetime import datetime


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id,
    )


def get_movies_sessions(session_date: str = None) -> MovieSession:
    if session_date:
        parsed_date = datetime.strptime(session_date, "%Y-%m-%d")
        return MovieSession.objects.filter(show_time__date=parsed_date)
    else:
        return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(pk=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: str = None,
        cinema_hall_id: int = None,
        movie_id: int = None,
) -> MovieSession:
    session = MovieSession.objects.get(pk=session_id)
    if show_time:
        session.show_time = show_time
    if cinema_hall_id:
        session.cinema_hall_id = cinema_hall_id
    if movie_id:
        session.movie_id = movie_id

    session.save()
    return session


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(pk=session_id).delete()
