from typing import Optional

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
    movie_show_time: str,
    movie_id: int,
    cinema_hall_id: int
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(
        session_date: Optional[str] = None
) -> QuerySet[MovieSession]:
    queryset = MovieSession.objects.all()

    if session_date is not None:
        queryset = queryset.filter(show_time__date=session_date)

    return queryset


def get_movie_session_by_id(movies_session_id: int) -> QuerySet[MovieSession]:
    return MovieSession.objects.get(id=movies_session_id)


def update_movie_session(
    session_id: Optional[int],
    show_time: Optional[str] = None,
    movie_id: Optional[str] = None,
    cinema_hall_id: Optional[int] = None
) -> None:

    update_session = get_movie_session_by_id(session_id)

    if show_time:
        update_session.show_time = show_time
    if movie_id:
        update_session.movie_id = movie_id
    if cinema_hall_id:
        update_session.cinema_hall_id = cinema_hall_id

    update_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
