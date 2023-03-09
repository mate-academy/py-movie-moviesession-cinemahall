from datetime import datetime

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> MovieSession:
    new_movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )

    return new_movie_session


def get_movies_sessions(session_date: str = None) -> QuerySet:
    queryset = MovieSession.objects.all()

    if session_date:
        year = session_date.split("-")[0]
        month = session_date.split("-")[1]
        day = session_date.split("-")[2]
        queryset = queryset.filter(show_time__year=year,
                                   show_time__month=month,
                                   show_time__day=day,)

    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> None:
    queryset = MovieSession.objects.filter(id=session_id)

    if show_time:
        queryset.update(
            show_time=show_time
        )

    if movie_id:
        queryset.update(
            movie_id=movie_id
        )

    if cinema_hall_id:
        queryset.update(
            cinema_hall_id=cinema_hall_id
        )


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
