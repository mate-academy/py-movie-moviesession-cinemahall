from db.models import Movie
from db.models import CinemaHall
from db.models import MovieSession


def create_movie_session(movie_show_time, movie_id: int, cinema_hall_id: int) -> None:
    get_cinema_hall_id = CinemaHall.objects.get(
        id=cinema_hall_id
    )
    get_movie_id = Movie.objects.get(
        id=movie_id
    )

    create_session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie=get_movie_id,
        cinema_hall=get_cinema_hall_id
    )
    return create_session


def get_movies_sessions(session_date=None) -> None:
    right_session_date = MovieSession.objects.all()
    if session_date is not None:
        return right_session_date.filter(show_time__date=session_date)
    else:
        return right_session_date


def get_movie_session_by_id(movie_session_id: int) -> int:
    right_movie_session_id = MovieSession.objects.get(id=movie_session_id)
    return right_movie_session_id


def update_movie_session(session_id: int,
                         show_time=None,
                         movie_id=None,
                         cinema_hall_id=None
                         ) -> None:
    if show_time:
        MovieSession.objects.all().update(show_time=show_time)
    if movie_id:
        MovieSession.objects.all().update(movie_id=movie_id)
    if cinema_hall_id:
        MovieSession.objects.all().update(cinema_hall_id=cinema_hall_id)


def delete_movie_session_by_id(session_id: int) -> None:
    return MovieSession.objects.filter(id=session_id).delete()
