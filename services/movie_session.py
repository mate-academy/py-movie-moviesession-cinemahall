from db.models import MovieSession, Movie, CinemaHall
from datetime import datetime


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
):
    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=cinema_hall,
        movie=movie
    )


def get_movies_sessions(session_date: str = None):
    movie_sessions = MovieSession.objects.all()

    if session_date is not None:
        date = datetime.strptime(session_date, "%Y-%m-%d").date()
        movie_sessions = movie_sessions.filter(show_time__date=date)

    return movie_sessions


def get_movie_session_by_id(movie_session_id: int):
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
):
    updated_movie = get_movie_session_by_id(session_id)

    if show_time is not None:
        updated_movie.show_time = show_time

    if movie_id is not None:
        updated_movie.movie_id = movie_id

    if cinema_hall_id is not None:
        updated_movie.cinema_hall_id = cinema_hall_id

    updated_movie.save()


def delete_movie_session_by_id(session_id: int):
    get_movie_session_by_id(session_id).delete()
