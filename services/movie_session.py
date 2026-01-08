from datetime import datetime
from django.db.models import QuerySet
from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)

    new_movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=cinema_hall,
        movie=movie
    )

    return new_movie_session


def get_movies_sessions(session_date: str = None) -> QuerySet:
    if session_date:
        try:
            session_date_obj = datetime.strptime(
                session_date,
                "%Y-%m-%d"
            ).date()
            movie_sessions = MovieSession.objects.filter(
                show_time__date=session_date_obj
            )
        except ValueError:
            raise ValueError(
                "Invalid date format. Expected format is 'YYYY-MM-DD'."
            )

    else:
        movie_sessions = MovieSession.objects.all()

    return movie_sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    updated_session = MovieSession.objects.get(
        id=session_id
    )

    if show_time:
        updated_session.show_time = show_time
    if movie_id:
        movie = Movie.objects.get(id=movie_id)
        updated_session.movie = movie
    if cinema_hall_id:
        cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
        updated_session.cinema_hall = cinema_hall

    updated_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    try:
        movie_session = MovieSession.objects.get(id=session_id)
        movie_session.delete()
    except MovieSession.DoesNotExist:
        raise ValueError(f"Movie session with id {session_id} does not exist.")
