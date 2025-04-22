from django.db.models import QuerySet

from db.models import MovieSession
import datetime


def create_movie_session(movie_show_time: datetime.datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> MovieSession:

    new_movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=cinema_hall_id,
        movie=movie_id,
    )

    return new_movie_session


def get_movies_sessions(session_date: str = None) -> QuerySet[MovieSession]:
    if session_date:
        try:
            datetime.strptime(session_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Use 'YYYY-MM-DD'.")
        return MovieSession.objects.get(show_time=session_date)

    return MovieSession.objects.all()


def update_movie_session(session_id: int,
                         show_time: datetime.datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> None:

    if session_id:
        session_to_update = MovieSession.objects.get(id=session_id)
        if show_time is not None:
            session_to_update.show_time = show_time
        if movie_id is not None:
            session_to_update.movie = movie_id
        if cinema_hall_id is not None:
            session_to_update.cinema_hall = cinema_hall_id

    session_to_update.save()


def delete_movie_session(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
