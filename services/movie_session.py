from datetime import datetime

from django.db.models.query import QuerySet

from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(
        session_date: str = None
) -> QuerySet[MovieSession]:
    queryset = MovieSession.objects.all()
    if session_date:
        queryset = queryset.filter(
            show_time__date=session_date
        )
    return queryset


def get_movie_session_by_id(
        movie_session_id: int
) -> MovieSession:
    return MovieSession.objects.get(pk=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    update_fields = {}
    if show_time is not None:
        update_fields["show_time"] = show_time
    if movie_id is not None:
        update_fields["movie_id"] = movie_id
    if cinema_hall_id is not None:
        update_fields["cinema_hall_id"] = cinema_hall_id

    if update_fields:
        MovieSession.objects.filter(pk=session_id).update(**update_fields)


def delete_movie_session_by_id(
        session_id: int
) -> None:
    MovieSession.objects.filter(pk=session_id).delete()
