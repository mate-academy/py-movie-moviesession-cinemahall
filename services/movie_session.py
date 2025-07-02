from datetime import datetime
from db.models import MovieSession, Movie, CinemaHall

def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int):
    movie = Movie.objects.get(pk= movie_id)
    cinema_hall = CinemaHall.objects.get(pk= cinema_hall_id)
    MovieSession.objects.create(show_time=movie_show_time,
                                movie=movie,
                                cinema_hall=cinema_hall)

def get_movies_sessions(session_date: str | None = None):
    return MovieSession.objects.filter(show_time=session_date)


def get_movie_session_by_id(movie_session_id: int):
    return MovieSession.objects.get(pk=movie_session_id)

def update_movie_session(
        session_id: int,
          show_time: datetime | None = None,
            movie_id: int | None = None,
              cinema_hall_id: int | None = None):
    session = get_movie_session_by_id(session_id)
    if show_time is not None:
        session.show_time = show_time
    if movie_id is not None:
        movie = Movie.objects.get(pk= movie_id)
        session.movie = movie
    if cinema_hall_id is not None:
        cinema_hall = CinemaHall.objects.get(pk= cinema_hall_id)
        session.cinema_hall = cinema_hall
    session.save()

def delete_movie_session_by_id(session_id: int):
    MovieSession.objects.filter(pk=session_id).delete()