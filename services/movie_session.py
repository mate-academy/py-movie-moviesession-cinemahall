import datetime

from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> None:

    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movies_sessions(
        session_date: datetime = None
) -> MovieSession.objects:

    queryset = MovieSession.objects.all()

    if session_date:
        queryset = queryset.filter(show_time__date=session_date)
    return queryset


def get_movie_session_by_id(
        session_id: int,
) -> MovieSession.objects:
    return MovieSession.objects.get(id=session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None,
) -> None:
    queryset = MovieSession.objects.get(id=session_id)

    if show_time:
        queryset.show_time = show_time
    if movie_id:
        queryset.movie_id = movie_id
    if cinema_hall_id:
        queryset.cinema_hall_id = cinema_hall_id

    queryset.save()


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
