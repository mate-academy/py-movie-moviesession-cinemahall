from django.db.models import QuerySet
from db.models import MovieSession, CinemaHall, Movie


def create_movie_session(
    movie_show_time: str,
    movie_id: int,
    cinema_hall_id: int
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinemahall=CinemaHall.objects.get(id=cinema_hall_id),
        movie=Movie.objects.get(id=movie_id)
    )


def get_movies_sessions(session_date: str = None) -> QuerySet | MovieSession:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
    session_id: int,
    show_time: str = None,
    movie_id: int = None,
    cinema_hall_id: int = None
) -> None:
    try:
        movie_session = MovieSession.objects.get(id=session_id)
    except MovieSession.DoesNotExist:
        raise ValueError(f"MovieSession with id {session_id} does not exist.")

    if show_time is not None:
        movie_session.show_time = show_time

    if movie_id is not None:
        try:
            movie_session.movie = Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            raise ValueError(f"Movie with id {movie_id} does not exist.")

    if cinema_hall_id is not None:
        try:
            movie_session.cinemahall = CinemaHall.objects.get(
                id=cinema_hall_id
            )
        except CinemaHall.DoesNotExist:
            raise ValueError(
                f"CinemaHall with id {cinema_hall_id} does not exist."
            )

    movie_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
