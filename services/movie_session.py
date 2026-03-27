from datetime import datetime

from django.db.models import QuerySet

from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    movie = Movie.objects.get(id=movie_id)
    hall = CinemaHall.objects.get(id=cinema_hall_id)
    session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie=movie,
        cinema_hall=hall
    )

    return session


def get_movie_session(session_date: datetime | None) -> QuerySet:
    if session_date is None:
        return MovieSession.objects.all()
    else:
        return MovieSession.objects.filter(show_time__date=session_date)


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime | None,
        movie_id: int | None,
        cinema_hall_id: int | None
) -> None:
    session = MovieSession.objects.get(id=session_id)
    if show_time is not None:
        session.show_time = show_time

    if movie_id is not None:
        try:
            session.movie = Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            return  # or raise

    if cinema_hall_id is not None:
        try:
            session.cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
        except CinemaHall.DoesNotExist:
            return  # or raise

    session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    return MovieSession.objects.get(id=session_id).delete()
