import datetime
from django.core.exceptions import ObjectDoesNotExist
from db.models import MovieSession, CinemaHall, Movie
from django.db.models.query import QuerySet


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int) -> None:
    MovieSession.objects.get_or_create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(
        session_date: str = None
) -> QuerySet[MovieSession]:
    if session_date:
        return MovieSession.objects.filter(
            show_time__date=session_date)
    else:
        return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    try:
        return MovieSession.objects.get(id=movie_session_id)
    except ObjectDoesNotExist:
        print(f"There is no session with id {movie_session_id} in the DB")


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    movie_session_to_update = MovieSession.objects.get(id=session_id)

    if show_time:
        movie_session_to_update.show_time = show_time
    if movie_id:
        movie_session_to_update.movie = Movie.objects.get(id=movie_id)
    if cinema_hall_id:
        movie_session_to_update.cinema_hall = CinemaHall.objects.get(
            id=cinema_hall_id
        )

    movie_session_to_update.save()


def delete_movie_session_by_id(session_id: int) -> None:
    get_movie_session_by_id(session_id).delete()
