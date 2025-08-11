from db.models import MovieSession
from django.db.models import QuerySet
from datetime import datetime


def create_movie_session(
        movie_show_time: datetime,
        cinema_hall_id: int = None,
        movie_id: int = None
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(
        session_date: str = None
) -> QuerySet:  # deep filtering
    if session_date:
        return MovieSession.objects.filter(
            show_time__date=datetime(
                *[int(num) for num in session_date.split("-")]
            )
        )
    else:
        return MovieSession.objects.all()


def get_movie_session_by_id(id_: int) -> MovieSession:
    return MovieSession.objects.get(id=id_)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    movie_session = MovieSession.objects.get(id=session_id)
    if show_time:
        movie_session.show_time = show_time
    if movie_id:
        movie_session.movie_id = movie_id
    if cinema_hall_id:
        movie_session.cinema_hall_id = cinema_hall_id
    movie_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
