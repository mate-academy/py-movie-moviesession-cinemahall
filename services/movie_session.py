from typing import List

from db.models import MovieSession


def create_movie_session(movie_show_time: str,
                         movie_id: int, cinema_hall_id: int) -> None:
    session = MovieSession.objects.create(show_time=movie_show_time)

    session.cinema_hall.add_movie(cinema_hall_id)
    session.add_movie(movie_id)

    session.save()


def get_movies_sessions(session_date: str = None) -> List[MovieSession]:
    if session_date:
        session = MovieSession.objects.filter(session_date)
        return session
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.filter(movie_id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: str = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> None:
    session = MovieSession.objects.get(id=session_id)

    if show_time:
        session.show_time = show_time

    if movie_id:
        session.movie_id = movie_id

    if cinema_hall_id:
        session.cinema_hall = cinema_hall_id

    session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
