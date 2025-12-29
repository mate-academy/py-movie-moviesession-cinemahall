import datetime

from django.db.models import QuerySet

from db.models import MovieSession, CinemaHall, Movie


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> QuerySet:
    cinema_hall = CinemaHall.objects.get(pk=cinema_hall_id)
    movie = Movie.objects.get(pk=movie_id)

    movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=cinema_hall,
        movie=movie
    )
    return movie_session


def get_movies_sessions(session_date: datetime = None) -> QuerySet:
    if session_date:
        date = datetime.datetime.strptime(session_date, "%Y-%m-%d")
        movie_sessions = MovieSession.objects.filter(show_time__date=date)
    else:
        movie_sessions = MovieSession.objects.all()

    return movie_sessions


def get_movie_session_by_id(movie_session_id: int) -> QuerySet:
    movie_sessions = MovieSession.objects.get(pk=movie_session_id)
    return movie_sessions


def update_movie_session(
        session_id: int | None = None,
        show_time: datetime = None,
        movie_id: int | None = None,
        cinema_hall_id: str | None = None
) -> QuerySet:
    movie_session = MovieSession.objects.filter(pk=session_id).first()
    if movie_session:
        if show_time is not None:
            movie_session.show_time = show_time
        if movie_id is not None:
            movie_session.movie_id = movie_id
        if cinema_hall_id is not None:
            movie_session.cinema_hall_id = cinema_hall_id
        movie_session.save()
    return movie_session


def delete_movie_session_by_id(session_id: int) -> None:
    movie_session = MovieSession.objects.get(pk=session_id)
    movie_session.delete()
