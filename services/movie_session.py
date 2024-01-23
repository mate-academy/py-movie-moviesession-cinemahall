from db.models import MovieSession, CinemaHall, Movie
from django.db.models import Model, QuerySet


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> Model:
    show_time = movie_show_time
    cinema_hall = CinemaHall.objects.get(pk=cinema_hall_id)
    movie = Movie.objects.get(pk=movie_id)
    movie_session = MovieSession.objects.create(
        show_time=show_time,
        cinema_hall=cinema_hall,
        movie=movie
    )
    return movie_session


def get_movies_sessions(movie_session: str = None) -> QuerySet:
    sessions = MovieSession.objects.all()
    if movie_session:
        sessions = sessions.filter(show_time__date=movie_session)
    return sessions


def get_movie_session_by_id(session_id: int) -> Model:
    return MovieSession.objects.get(id=session_id)


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None) -> None:
    session = get_movie_session_by_id(session_id)

    if show_time:
        session.show_time = show_time

    if movie_id:
        session.movie_id = movie_id

    if cinema_hall_id:
        session.cinema_hall_id = cinema_hall_id

    session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    get_movie_session_by_id(session_id).delete()
