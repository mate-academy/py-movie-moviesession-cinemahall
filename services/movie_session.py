from db.models import MovieSession
from django.db.models import QuerySet


def get_movies_sessions(session_date: str = None) -> QuerySet:
    queryset = MovieSession.objects.all()
    if session_date:
        queryset = queryset.filter(show_time__date=session_date)

    return queryset


def get_movie_session_by_id(movie_session_id: int) -> QuerySet:
    if movie_session_id:
        return MovieSession.objects.get(id=movie_session_id)


def create_movie_session(movie_show_time: str,
                         movie_id: int, cinema_hall_id: int
                         ) -> None:
    new_movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id)

    return new_movie_session


def update_movie_session(session_id: int,
                         show_time: str = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None
                         ) -> None:
    up_session = get_movie_session_by_id(session_id)
    if show_time:
        up_session.show_time = show_time
    if movie_id:
        up_session.movie_id = movie_id
    if cinema_hall_id:
        up_session.cinema_hall_id = cinema_hall_id
    up_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    if session_id:
        get_movie_session_by_id(session_id).delete()
