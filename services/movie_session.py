from django.db.models import QuerySet

from db.models import MovieSession

from datetime import datetime


def create_movie_session(movie_show_time: datetime,
                         movie_id: int, cinema_hall_id: int) -> MovieSession:
    return MovieSession.objects.create(show_time=movie_show_time,
                                       cinema_hall_id=cinema_hall_id,
                                       movie_id=movie_id)


def get_movies_sessions(session_date: str = None) -> QuerySet:
    queryset = MovieSession.objects.all()
    if session_date:
        return queryset.filter(show_time__date=session_date)
    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(pk=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: datetime = None,
                         cinema_hall_id: int = None,
                         movie_id: int = None) -> None:
    moviesess = MovieSession.objects.get(id=session_id)
    if show_time:
        moviesess.show_time = show_time
        moviesess.save()

    if cinema_hall_id:
        moviesess.cinema_hall_id = cinema_hall_id
        moviesess.save()

    if movie_id:
        moviesess.movie_id = movie_id
        moviesess.save()


def delete_movie_session_by_id(session_id: int) -> None:
    return MovieSession.objects.get(id=session_id).delete()
