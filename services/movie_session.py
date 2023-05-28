from typing import Optional
from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(
    movie_show_time: str, movie_id: int, cinema_hall_id: int
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=CinemaHall.objects.get(id=cinema_hall_id),
        movie=Movie.objects.get(id=movie_id),
    )


def get_movies_sessions(
    session_date: Optional[str] = None,
) -> list[MovieSession]:
    if session_date is None:
        return MovieSession.objects.all()
    return MovieSession.objects.filter(show_time__date=session_date)


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
    session_id: int,
    show_time: Optional[str] = None,
    movie_id: Optional[int] = None,
    cinema_hall_id: Optional[int] = None,
) -> None:
    movie_session = get_movie_session_by_id(session_id)
    if show_time is not None:
        movie_session.show_time = show_time
    if movie_id is not None:
        movie_session.movie = Movie.objects.get(id=movie_id)
    if cinema_hall_id is not None:
        movie_session.cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    movie_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    movie_session = get_movie_session_by_id(session_id)
    movie_session.delete()
