from db.models import MovieSession, CinemaHall, Movie
from django.db.models import QuerySet
from datetime import datetime


def create_movie_session(movie_show_time: datetime, movie_id: int,
                         cinema_hall_id: int) -> MovieSession:
    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)

    new_session = MovieSession.objects.create(show_time=movie_show_time,
                                              movie=movie,
                                              cinema_hall=cinema_hall)

    return new_session


def get_movies_sessions(
        session_date: str | None = None) -> QuerySet[MovieSession]:
    queryset = MovieSession.objects.all()

    if session_date:
        query_date = datetime.strptime(session_date, "%Y-%m-%d")
        queryset = queryset.filter(show_time__date=query_date.date())

    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: type(datetime.date) | None = None,
                         movie_id: int | None = None,
                         cinema_hall_id: int | None = None) -> None:
    new_session = {}

    if show_time:
        new_session["show_time"] = show_time

    if movie_id:
        new_session["movie"] = Movie.objects.get(id=movie_id)

    if cinema_hall_id:
        new_session["cinema_hall"] = CinemaHall.objects.get(id=cinema_hall_id)

    if new_session.keys:
        MovieSession.objects.filter(id=session_id).update(**new_session)


def delete_movie_session_by_id(session_id: int) -> None:
    movie_to_delete = get_movie_session_by_id(session_id)

    movie_to_delete.delete()
