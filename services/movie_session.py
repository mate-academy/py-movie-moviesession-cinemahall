from django.db.models import QuerySet
from db.models import MovieSession, CinemaHall, Movie


def create_movie_session(
        movie_show_time: str,
        movie_id: list[int],
        cinema_hall_id: list[int]
) -> MovieSession:
    movie_id = Movie.objects.get(id=movie_id)
    cinema_hall_id = CinemaHall.objects.get(id=cinema_hall_id)
    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=cinema_hall_id,
        movie=movie_id
    )


def get_movies_sessions(
        session_date: str = None
) -> QuerySet[MovieSession] | None:
    queryset = MovieSession.objects.all()
    if session_date:
        queryset = MovieSession.objects.filter(show_time__date=session_date)
    return queryset


def get_movie_session_by_id(
        movie_session_id: int
) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None

) -> QuerySet[MovieSession] | None:
    session_date_movie = MovieSession.objects.get(id=session_id)
    if show_time:
        session_date_movie.show_time = show_time
    if movie_id:
        session_date_movie.movie_id = movie_id
    if cinema_hall_id:
        session_date_movie.cinema_hall_id = cinema_hall_id

    session_date_movie.save()

    return session_date_movie


def delete_movie_session_by_id(
        session_id: int
) -> None:
    session_date_movie = MovieSession.objects.get(id=session_id)
    session_date_movie.delete()
