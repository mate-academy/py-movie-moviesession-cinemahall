from django.db.models import QuerySet
from db.models import MovieSession, CinemaHall, Movie
from datetime import datetime


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> None:

    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    movie = Movie.objects.get(id=movie_id)

    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=cinema_hall,
        movie=movie,
    )


def get_movies_sessions(
        session_date: str = None
) -> QuerySet:

    if session_date:
        date_obj = datetime.strptime(session_date, "%Y-%m-%d")
        result = MovieSession.objects.filter(show_time__date=date_obj)
    else:
        result = MovieSession.objects.all()

    return result


def get_movie_session_by_id(
        movie_id: int
) -> MovieSession:

    return MovieSession.objects.get(id=movie_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None,
) -> None:

    session = MovieSession.objects.get(id=session_id)

    if show_time:
        session.show_time = show_time
    if movie_id:
        movie = Movie.objects.get(id=movie_id)
        session.movie_id = movie
    if cinema_hall_id:
        cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
        session.cinema_hall = cinema_hall

    session.save()


def delete_movie_session_by_id(session_id: int) -> None:

    session = MovieSession.objects.get(id=session_id)
    session.delete()
