from datetime import datetime

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int

) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(
        session_date: str = None,
) -> QuerySet:
    queryset = MovieSession.objects.all()
    if session_date:
        queryset = queryset.filter(
            show_time__date=datetime.strptime(session_date, "%Y-%m-%d")
        )
    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(
        id=movie_session_id
    )


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        cinema_hall_id: int = None,
        movie_id: int = None
) -> None:
    session_to_update = get_movie_session_by_id(session_id)

    if show_time:
        session_to_update.show_time = show_time

    if cinema_hall_id:
        session_to_update.cinema_hall_id = cinema_hall_id

    if movie_id:
        session_to_update.movie_id = movie_id

    session_to_update.save()


def delete_movie_session_by_id(session_id: int) -> None:
    get_movie_session_by_id(session_id).delete()
