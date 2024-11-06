from db.models import MovieSession, Movie, CinemaHall

from django.db.models import QuerySet

from datetime import datetime


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie=Movie.objects.get(id=movie_id),
        cinema_hall=CinemaHall.objects.get(id=cinema_hall_id)
    )


def get_movies_sessions(
        session_date: datetime = None
) -> QuerySet[MovieSession] | MovieSession:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> MovieSession:
    updated_movie_session = MovieSession.objects.filter(
        id=session_id
    )

    if show_time:
        updated_movie_session.update(show_time=show_time)
    if movie_id:
        updated_movie_session.update(movie=movie_id)
    if cinema_hall_id:
        updated_movie_session.update(cinema_hall=cinema_hall_id)

    return updated_movie_session


def delete_movie_session_by_id(session_id: int) -> MovieSession:
    return MovieSession.objects.filter(id=session_id).delete()
