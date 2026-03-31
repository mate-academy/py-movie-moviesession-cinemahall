from datetime import datetime

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> MovieSession:

    movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )
    return movie_session


def get_movies_sessions(
        session_date: str = None
) -> QuerySet[MovieSession]:
    if session_date is None:
        return MovieSession.objects.all()
    date_obj = datetime.strptime(session_date, "%Y-%m-%d").date()
    return MovieSession.objects.filter(show_time__date=date_obj)


def get_movie_session_by_id(
        movie_session_id: int = None,
) -> MovieSession:
    if movie_session_id is None:
        return MovieSession.objects.all()
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int = None,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None,
) -> MovieSession | None:
    if session_id:
        movie_session = MovieSession.objects.get(id=session_id)
        if movie_session:
            if show_time:
                movie_session.show_time = show_time
            if movie_id:
                movie_session.movie_id = movie_id
            if cinema_hall_id:
                movie_session.cinema_hall_id = cinema_hall_id
            movie_session.save()
            return movie_session
    return None


def delete_movie_session_by_id(session_id: int) -> None:
    movie_session = get_movie_session_by_id(session_id)
    movie_session.delete()
