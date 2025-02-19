from xmlrpc.client import DateTime

from django.db.models import QuerySet

from db.models import Movie, CinemaHall, MovieSession


def create_movie_session(movie_show_time: DateTime,
                         movie_id: int,
                         cinema_hall_id: int) -> MovieSession:
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    movie = Movie.objects.get(id=movie_id)
    return MovieSession.objects.create(show_time=movie_show_time,
                                       cinema_hall=cinema_hall,
                                       movie=movie)


def get_movies_sessions(*args, **kwargs) -> QuerySet:
    session_date = None
    if args:
        session_date = args[0]
    if kwargs:
        session_date = kwargs["session_date"]

    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: DateTime = None,
                         cinema_hall_id: int = None,
                         movie_id: int = None,) -> None:
    movie_session = MovieSession.objects.get(id=session_id)

    if show_time:
        movie_session.show_time = show_time
    if cinema_hall_id:
        movie_session.cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    if movie_id:
        movie_session.movie_id = movie_id
    movie_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
