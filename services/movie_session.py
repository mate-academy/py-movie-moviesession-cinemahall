from django.db.models import QuerySet

from db.models import MovieSession
import datetime


def create_movie_session(movie_show_time: datetime.datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> MovieSession:

    new_movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id,
    )

    return new_movie_session


def get_movies_sessions(session_date: str = None) -> QuerySet[MovieSession]:
    queryset = MovieSession.objects.all()
    if session_date:
        try:
            datetime.strptime(session_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Use 'YYYY-MM-DD'.")
        return queryset.filter(show_time__date=session_date)

    return queryset


def update_movie_session(session_id: int,
                         show_time: datetime.datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> None:

    if session_id:
        session_to_update = MovieSession.objects.get(id=session_id)
        if show_time is not None:
            session_to_update.show_time = show_time
        if movie_id is not None:
            session_to_update.movie_id = movie_id
        if cinema_hall_id is not None:
            session_to_update.cinema_hall_id = cinema_hall_id

        session_to_update.save()


def delete_movie_session(session_id: int) -> None:
    sessions = MovieSession.objects.all()
    sessions.filter(id=session_id).delete()
