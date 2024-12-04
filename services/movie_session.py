from django.utils.dateparse import parse_date
from db.models import Movie, CinemaHall, MovieSession


def create_movie_session(movie_show_time: int |float,
                         movie_id: id,
                         cinema_hall_id: int) -> Movie | CinemaHall:
    movie=Movie.objects.get(id=movie_id)
    cinema_hall=CinemaHall.objects.get(id=cinema_hall_id)
    return Movie.objects.create(
        movie_show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id)


def get_movies_sessions(session_date: str) -> list[Movie | CinemaHall]:
    if session_date:
        date=parse_date(session_date)
        return MovieSession.objects.filter(show__time__date=date)
    else:
        return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> Movie | CinemaHall:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: int | float,
                         movie_id: int,
                         cinema_hall_id: int) -> Movie | CinemaHall:
    movie_session = MovieSession.objects.get(id=session_id)
    if show_time:
        movie_session.show_time=show_time
    if movie_id:
        movie=Movie.objects.get(id=movie_id)
        movie_session.movie=movie
    if cinema_hall_id:
        cinema_hall=CinemaHall.objects.get(id=cinema_hall_id)
        movie_session.cinema_hall=cinema_hall
    movie_session.save()
    return movie_session


def delete_movie_session_by_id(session_id: int) -> Movie | CinemaHall:
    return MovieSession.objects.get(id=session_id).delete()
