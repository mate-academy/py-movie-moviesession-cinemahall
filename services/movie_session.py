from django.db.models.query import QuerySet
from db.models import MovieSession


def create_movie_session(movie_show_time: int,
                         movie_id: int,
                         cinema_hall_id: int) -> QuerySet:

    new_session = MovieSession.objects.create(show_time=movie_show_time,
                                              cinema_hall_id=cinema_hall_id,
                                              movie_id=movie_id)

    return new_session


def get_movies_sessions(session_date: str = None) -> QuerySet:

    queryset = MovieSession.objects.all()

    if session_date:
        queryset = queryset.filter(show_time__date=session_date)

    return queryset


def get_movie_session_by_id(movie_session_id: int) -> QuerySet:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: str = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> QuerySet:

    movie = MovieSession.objects.get(id=session_id)

    if show_time:
        movie.show_time = show_time

    if movie_id:
        movie.movie_id = movie_id

    if cinema_hall_id:
        movie.cinema_hall_id = cinema_hall_id

    movie.save()
    return movie


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
