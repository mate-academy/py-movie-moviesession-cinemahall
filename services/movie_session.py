from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movies_sessions(session_date: str = None) -> QuerySet:
    movies_sessions = MovieSession.objects.all()
    if session_date:
        return movies_sessions.filter(show_time__date=session_date)
    return movies_sessions


def get_movie_session_by_id(movie_session_id: int) -> QuerySet:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None) -> MovieSession:
    movie_session_update = get_movie_session_by_id(session_id)
    if show_time:
        movie_session_update.show_time = show_time
    if movie_id:
        movie_session_update.movie_id = movie_id
    if cinema_hall_id:
        movie_session_update.cinema_hall_id = cinema_hall_id

    movie_session_update.save()


def delete_movie_session_by_id(session_id: int) -> None:
    get_movie_session_by_id(session_id).delete()
