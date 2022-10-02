import datetime

from db.models import MovieSession, CinemaHall, Movie


def create_movie_session(movie_show_time: datetime, movie_id: int,
                         cinema_hall_id: int):
    cinema = CinemaHall.objects.get(id=cinema_hall_id)
    movie_ = Movie.objects.get(id=movie_id)
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=cinema,
        movie=movie_
    )


def get_movies_sessions(session_date: str = None):
    if session_date is not None:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int):
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
):
    session = MovieSession.objects.get(id=session_id)
    if show_time is not None:
        session.show_time = show_time
    if movie_id is not None:
        session.movie_id = movie_id
    if cinema_hall_id is not None:
        session.cinema_hall_id = cinema_hall_id
    session.save()


def delete_movie_session_by_id(session_id: int):
    MovieSession.objects.get(id=session_id).delete()
