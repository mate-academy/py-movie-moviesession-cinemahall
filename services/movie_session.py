import datetime

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(movie_show_time: datetime.datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> MovieSession:
    return MovieSession.objects.create(show_time=movie_show_time,
                                       cinema_hall=cinema_hall_id,
                                       movie=movie_id)


def get_movies_sessions(session_date: str | None = None) -> QuerySet:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> QuerySet:
    return MovieSession.objects.filter(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: datetime.datetime | None = None,
                         movie_id: int | None = None,
                         cinema_hall_id: int | None = None) -> QuerySet:
    movie_session = MovieSession.objects.filter(id=session_id)

    if show_time:
        movie_session.update(show_time = show_time)
    if movie_id:
        movie_session.update(movie=movie_id)
    if cinema_hall_id:
        movie_session.update(cinema_hall=cinema_hall_id)

    return movie_session

def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
