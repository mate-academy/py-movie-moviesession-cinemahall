from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:

    new_movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie=movie_id,
        cinema_hall=cinema_hall_id
    )

    return new_movie_session


def get_movies_sessions(session_date: str = None) -> QuerySet:

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
) -> MovieSession:

    update_movie = MovieSession.objects.get(id=session_id)

    if show_time:
        update_movie.show_time = show_time

    if movie_id:
        update_movie.movie = movie_id

    if cinema_hall_id:
        update_movie.cinema_hall = cinema_hall_id

    update_movie.save()

    return update_movie


def delete_movie_session_by_id(session_id: int) -> None:
    return MovieSession.objects.delete(id=session_id)
