from datetime import datetime

from db.models import MovieSession, CinemaHall, Movie


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    cinema_hall_inst = CinemaHall.objects.get(id=cinema_hall_id)
    movie_inst = Movie.objects.get(id=movie_id)
    new_session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=cinema_hall_inst,
        movie=movie_inst,
    )

    return new_session


def get_movies_sessions(session_date: str = None) -> None:
    queryset = MovieSession.objects.all()

    if session_date:
        queryset = queryset.filter(show_time__date=session_date)

    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> MovieSession:
    session_for_update = MovieSession.objects.get(id=session_id)

    if show_time:
        session_for_update.show_time = show_time

    if movie_id:
        session_for_update.movie_id = movie_id

    if cinema_hall_id:
        session_for_update.cinema_hall_id = cinema_hall_id

    session_for_update.save()
    return session_for_update


def delete_movie_session_by_id(session_id: int) -> None:
    session_for_delete = MovieSession.objects.get(id=session_id)
    session_for_delete.delete()
