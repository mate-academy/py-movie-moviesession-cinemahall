from db.models import MovieSession, CinemaHall, Movie
import datetime


def create_movie_session(
        movie_show_time: datetime.datetime,
        movie_id: int,
        cinema_hall_id: int,
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=CinemaHall.objects.get(id=cinema_hall_id),
        movie=Movie.objects.get(id=movie_id)
    )


def get_movies_sessions(
        session_date: datetime.date = None
) -> list[MovieSession]:
    sessions = MovieSession.objects.all()

    if session_date is not None:
        sessions = sessions.filter(show_time__date=session_date)

    return sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime.datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None,
) -> None:
    session = MovieSession.objects.filter(id=session_id)
    if show_time is not None:
        session.update(show_time=show_time)
    if movie_id is not None:
        session.update(movie=movie_id)
    if cinema_hall_id is not None:
        session.update(cinema_hall=cinema_hall_id)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
