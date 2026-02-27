from django.db.models import QuerySet
from django.core.exceptions import ObjectDoesNotExist

from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    movie = Movie.objects.get(id=movie_id)
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=cinema_hall,
        movie=movie
    )


def get_movies_sessions(
        session_date: str = None
) -> QuerySet[MovieSession] | MovieSession:
    sessions = MovieSession.objects.all()
    if session_date:
        sessions = sessions.filter(show_time__date=session_date)
    return sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession | str:
    try:
        return MovieSession.objects.get(id=movie_session_id)
    except ObjectDoesNotExist:
        return f"Movie session with id{movie_session_id} does not exist"


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None | str:
    try:
        session = MovieSession.objects.get(id=session_id)

        if show_time:
            session.show_time = show_time
        if movie_id:
            try:
                session.movie = Movie.objects.get(id=movie_id)
            except ObjectDoesNotExist:
                return f"Movie with id {movie_id} does not exist."
        if cinema_hall_id:
            try:
                session.cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
            except ObjectDoesNotExist:
                return f"CinemaHall with id {cinema_hall_id} does not exist."
        session.save()
    except ObjectDoesNotExist:
        return f"MovieSession with id {session_id} does not exist."


def delete_movie_session_by_id(session_id: int) -> None | str:
    try:
        MovieSession.objects.get(id=session_id).delete()
    except ObjectDoesNotExist:
        return f"Movie session with id{session_id} does not exist"
