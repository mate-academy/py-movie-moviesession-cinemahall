import datetime


from django.db.models import QuerySet
from db.models import MovieSession, CinemaHall, Movie


def create_movie_session(movie_show_time: datetime.datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> None:
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    MovieSession.objects.create(show_time=movie_show_time,
                                movie=Movie.objects.get(id=movie_id),
                                cinema_hall=cinema_hall)


def get_movies_sessions(session_date: datetime.datetime = None) -> QuerySet:
    if session_date:
        date = datetime.date(*list(map(int, session_date.split("-"))))
        return MovieSession.objects.filter(show_time__date=date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: datetime.datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> None:
    if show_time:
        MovieSession.objects.filter(id=session_id).update(show_time=show_time)
    if cinema_hall_id:
        (MovieSession.objects.filter(id=session_id)
         .update(cinema_hall=CinemaHall.objects.get(id=cinema_hall_id)))
    if movie_id:
        (MovieSession.objects.filter(id=session_id)
         .update(movie=Movie.objects.get(id=movie_id)))


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
