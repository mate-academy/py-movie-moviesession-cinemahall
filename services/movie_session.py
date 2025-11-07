from db.models import MovieSession, Movie, CinemaHall
from datetime import datetime


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> MovieSession:
    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=cinema_hall,
        movie=movie
    )
    return movie_session

def get_movies_sessions(session_date: str=None) -> "QuerySet[MovieSession]":
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    else:
        return MovieSession.objects.all()

def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.filter(id=movie_session_id).first()

def update_movie_session(session_id: int,
                         show_time: str=None,
                         movie_id: int=None,
                         cinema_hall_id: int=None
                         ) -> MovieSession:
    movie_session = MovieSession.objects.filter(id=session_id).first()
    if movie_session:
        if show_time:
            movie_session.show_time = show_time
            movie_session.save()
        if movie_id:
            movie_session.movie = Movie.objects.get(id=movie_id)
            movie_session.save()
        if cinema_hall_id:
            movie_session.cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
            movie_session.save()
    return movie_session

def delete_movie_session_by_id(session_id: int) -> None:
    movie_session = get_movie_session_by_id(session_id)
    if movie_session:
        movie_session.delete()
