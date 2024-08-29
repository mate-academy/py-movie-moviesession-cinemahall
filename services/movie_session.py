from db.models import MovieSession, CinemaHall, Movie
from datetime import datetime
from django.db.models import QuerySet


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


def get_movies_sessions(session_date: str = None) -> QuerySet[MovieSession]:
    queryset = MovieSession.objects.all()
    if session_date:
        session_date = datetime.strptime(session_date, "%Y-%m-%d")
        queryset = queryset.filter(show_time__date=session_date.date())
    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(pk=movie_session_id)


def update_movie_session(
    session_id: int,
    show_time: datetime = None,
    movie_id: int = None,
    cinema_hall_id: int = None
) -> None:
    updates = {}
    if show_time:
        updates["show_time"] = show_time
    if movie_id:
        updates["movie"] = Movie.objects.get(pk=movie_id)
    if cinema_hall_id:
        updates["cinema_hall"] = CinemaHall.objects.get(pk=cinema_hall_id)

    if updates:
        MovieSession.objects.filter(
            pk=session_id
        ).update(**updates)


def delete_movie_session_by_id(session_id: int) -> None:
    get_movie_session_by_id(session_id).delete()
