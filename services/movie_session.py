from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(movie_show_time: str,
                         movie_id: int,
                         cinema_hall_id: int) -> MovieSession:
    new_movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )
    return new_movie_session


def get_movies_sessions(session_date: str = None) -> QuerySet:
    sessions = MovieSession.objects.all()

    if session_date:
        sessions = sessions.filter(show_time__year=session_date.split("-")[0],
                                   show_time__month=session_date.split("-")[1],
                                   show_time__day=session_date.split("-")[2])

    return sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    if MovieSession.objects.filter(id=movie_session_id).exists():
        return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: str = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> MovieSession | None:
    if MovieSession.objects.filter(id=session_id).exists():
        session = MovieSession.objects.get(id=session_id)
    else:
        return

    if show_time:
        session.show_time = show_time

    if movie_id:
        session.movie_id = movie_id

    if cinema_hall_id:
        session.cinema_hall_id = cinema_hall_id

    session.save()

    return session


def delete_movie_session_by_id(session_id: int) -> None:
    if MovieSession.objects.filter(id=session_id).exists():
        MovieSession.objects.get(id=session_id).delete()
