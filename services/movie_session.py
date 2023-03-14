from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movies_sessions(session_date: str = None) -> QuerySet[MovieSession]:
    movies_sessions = MovieSession.objects.all()
    if session_date is not None:
        movies_sessions = MovieSession.objects.filter(
            show_time__date=session_date
        )
    return movies_sessions


def get_movie_session_by_id(movie_session_id: int) -> QuerySet[MovieSession]:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    if show_time is not None:
        MovieSession.objects.filter(id=session_id).update(show_time=show_time)
    if movie_id is not None:
        MovieSession.objects.filter(id=session_id).update(movie=movie_id)
    if cinema_hall_id is not None:
        MovieSession.objects.filter(
            id=session_id
        ).update(cinema_hall=cinema_hall_id)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
