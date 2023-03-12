from db.models import MovieSession
import datetime


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movies_sessions(session_date: str = None) -> MovieSession:
    movies = MovieSession.objects.all()
    if session_date:
        movies = movies.filter(show_time__date=session_date)
    return movies


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: str = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> MovieSession:
    movie = MovieSession.objects.filter(id=session_id)
    if show_time:
        movie.update(
            show_time=show_time
        )
    if movie_id:
        movie.update(
            movie_id=movie_id
        )
    if cinema_hall_id:
        movie.update(
            cinema_hall=cinema_hall_id
        )
    return movie


def delete_movie_session_by_id(session_id: int) -> None:
    movie = MovieSession.objects.filter(id=session_id)
    return movie.delete()
