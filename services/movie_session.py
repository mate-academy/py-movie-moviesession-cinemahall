import datetime

from django.db.models import QuerySet

from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(
        movie_show_time: datetime.datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    movie_key = Movie.objects.get(id=movie_id)
    cinema_hall_key = CinemaHall.objects.get(id=cinema_hall_id)

    new_movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie=movie_key,
        cinema_hall=cinema_hall_key
    )

    return new_movie_session


def get_movies_sessions(session_date: str = None) -> QuerySet:
    queryset = MovieSession.objects.all()
    if session_date:
        queryset = MovieSession.objects.filter(show_time__date=session_date)
    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime.datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> MovieSession:
    session_to_update = MovieSession.objects.filter(id=session_id)

    if show_time:
        session_to_update.update(show_time=show_time)

    if movie_id:
        movie_key = Movie.objects.get(id=movie_id)
        session_to_update.update(movie=movie_key)

    if cinema_hall_id:
        cinema_hall_key = CinemaHall.objects.get(id=cinema_hall_id)
        session_to_update.update(cinema_hall=cinema_hall_key)

    return session_to_update


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
