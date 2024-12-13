from xmlrpc.client import DateTime

from django.db.models import QuerySet

from db.models import MovieSession, Movie, CinemaHall


def get_movie_session(movie_session_id: int) -> MovieSession:
    try:
        return MovieSession.objects.get(id=movie_session_id)
    except MovieSession.DoesNotExist:
        return None


def create_movie_session(movie_show_time: DateTime,
                         movie_id: int,
                         cinema_hall_id: int) -> MovieSession:
    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    return MovieSession.objects.create(show_time=movie_show_time,
                                       movie=movie, cinema_hall=cinema_hall)


def delete_movie_session_by_id(movie_session_id: int) -> None:
    MovieSession.objects.filter(id=movie_session_id).delete()


def get_movies_sessions(session_date: DateTime = None) -> QuerySet:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def update_movie_session(session_id: int,
                         show_time: DateTime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> MovieSession:
    session = MovieSession.objects.get(id=session_id)
    if show_time:
        session.show_time = show_time
    if movie_id:
        session.movie = Movie.objects.get(id=movie_id)
    if cinema_hall_id:
        session.cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    session.save()
    return session
