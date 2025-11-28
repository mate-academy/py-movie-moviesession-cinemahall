import datetime
from django.db.models import QuerySet
from db.models import MovieSession


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id,
    )


def get_movies_sessions(session_date: str = None) -> QuerySet:
    queryset = MovieSession.objects.all()
    if session_date:
        parsed = datetime.datetime.strptime(session_date, "%Y-%m-%d").date()
        queryset = queryset.filter(show_time__date=parsed)
    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> MovieSession:
    obj = MovieSession.objects.get(id=session_id)
    if show_time:
        obj.show_time = show_time
    if movie_id:
        obj.movie_id = movie_id
    if cinema_hall_id:
        obj.cinema_hall_id = cinema_hall_id
    obj.save()
    return obj


def delete_movie_session_by_id(session_id: int) -> str:
    movie_session = MovieSession.objects.get(id=session_id)
    movie_session.delete()
    return "Successfully deleted!"
