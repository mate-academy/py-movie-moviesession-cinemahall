from datetime import datetime

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id,
    )


def get_movies_sessions(
        session_date: str = None,
) -> QuerySet[MovieSession]:
    queryset = MovieSession.objects.all()
    if session_date:
        date = datetime.strptime(session_date, "%Y-%m-%d")
        queryset = queryset.filter(
            show_time__year=date.year,
            show_time__month=date.month,
            show_time__day=date.day
        )
    return queryset


def get_movie_session_by_id(
        movie_session_id: int
) -> MovieSession:
    try:
        return MovieSession.objects.get(id=movie_session_id)
    except MovieSession.DoesNotExist:
        print(f"MovieSession with id {movie_session_id} does not exist")


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None,
) -> None:
    movie_session = MovieSession.objects.filter(id=session_id)
    if show_time:
        movie_session.update(
            show_time=show_time,
        )
    if movie_id:
        movie_session.update(
            movie_id=movie_id,
        )
    if cinema_hall_id:
        movie_session.update(
            cinema_hall_id=cinema_hall_id,
        )


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
