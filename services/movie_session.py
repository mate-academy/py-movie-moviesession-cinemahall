from datetime import datetime, timedelta
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import QuerySet
from db.models import MovieSession, CinemaHall, Movie


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    if isinstance(movie_show_time, str):
        try:
            show_time = datetime.strptime(movie_show_time, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Date format must be 'YYYY-MM-DD'")
    elif isinstance(movie_show_time, datetime):
        show_time = movie_show_time
    else:
        raise TypeError("movie_show_time must be a string or datetime object")

    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)

    MovieSession.objects.create(
        show_time=show_time,
        movie=movie,
        cinema_hall=cinema_hall
    )


def get_movies_sessions(session_date: str = None) -> MovieSession | QuerySet:
    """
    Process a date in the format "YYYY-MM-DD".
    """
    if session_date:
        start_date = datetime.strptime(session_date, "%Y-%m-%d")
        end_date = start_date + timedelta(days=1)

        return (MovieSession.objects
                .filter(show_time__gte=start_date, show_time__lt=end_date))

    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    update_fields = {}
    if show_time is not None:
        update_fields["show_time"] = show_time

    if movie_id is not None:
        try:
            Movie.objects.get(id=movie_id)
            update_fields["movie_id"] = movie_id
        except ObjectDoesNotExist:
            raise ValueError(f"Movie with id {movie_id} does not exist.")

    if cinema_hall_id is not None:
        try:
            CinemaHall.objects.get(id=cinema_hall_id)
            update_fields["cinema_hall_id"] = cinema_hall_id
        except ObjectDoesNotExist:
            raise ValueError(f"CinemaHall with "
                             f"id {cinema_hall_id} does not exist.")

    if update_fields:
        MovieSession.objects.filter(id=session_id).update(**update_fields)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
