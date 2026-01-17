from db.models import MovieSession

from django.db.models import QuerySet


def create_movie_session(
        movie_show_time: MovieSession,
        movie_id: MovieSession,
        cinema_hall_id: MovieSession
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id,
    )


def get_movies_sessions(
        session_date: str = None
) -> MovieSession | QuerySet[MovieSession]:
    if session_date:
        return MovieSession.objects.get(__date=session_date)
    else:
        return MovieSession.objects.all()


def get_movie_session_by_id(
        movie_session_id: int
) -> MovieSession | QuerySet[MovieSession]:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: int = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    MovieSession.objects.get(id=session_id).update(
        show_time, movie_id, cinema_hall_id, movie_id
    )


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
