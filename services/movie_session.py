from django.db.models import QuerySet
from django.db.models.fields import DateTimeField

from db.models import Movie, MovieSession, CinemaHall


def create_movie_session(
        movie_show_time: DateTimeField,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        movie=Movie.objects.get(id=movie_id),
        show_time=movie_show_time,
        cinema_hall=CinemaHall.objects.get(id=cinema_hall_id)
    )


def get_movies_sessions(  # by date
        session_date: DateTimeField = None
) -> QuerySet[MovieSession]:
    if session_date:
        return MovieSession.objects.all().filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(
        movie_session_id: int
) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: DateTimeField = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    session = MovieSession.objects.get(id=session_id)
    if show_time:
        session.show_time = show_time
    if movie_id:
        session.movie = Movie.objects.get(id=movie_id)
    if cinema_hall_id:
        session.cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
