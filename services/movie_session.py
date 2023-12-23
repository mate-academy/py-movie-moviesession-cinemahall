from typing import List


from db.models import MovieSession


from datetime import datetime


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> None:

    MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id)


def get_movies_sessions(session_date: str = None) -> List[MovieSession]:
    queryset = MovieSession.objects.all()
    if session_date:
        queryset = queryset.filter(show_time__date=session_date)
    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:

    update_move_session = get_movie_session_by_id(session_id)

    if show_time:
        update_move_session.show_time = show_time
    if movie_id:
        update_move_session.movie_id = movie_id
    if cinema_hall_id:
        update_move_session.cinema_hall_id = cinema_hall_id

    update_move_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    delete_move_session = get_movie_session_by_id(session_id)
    delete_move_session.delete()
