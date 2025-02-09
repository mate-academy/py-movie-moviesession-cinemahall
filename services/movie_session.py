from datetime import datetime

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> MovieSession:
    inst = MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )
    # if inst and movie_id:
    #     inst.movie.set(movie_id)
    # if inst and cinema_hall_id:
    #     inst.cinema_hall.set(cinema_hall_id)

    return inst


def get_movies_sessions(session_date: str = None) -> QuerySet:
    # year, month, day = session_date.split("-")
    queryset = MovieSession.objects.all()
    if session_date:
        queryset = queryset.filter(show_time__date=session_date)
    return queryset


def get_movie_session_by_id(movie_session_id: int = None) -> MovieSession:
    if movie_session_id:
        return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int = None,
                         show_time: datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> None:
    if session_id:
        inst = MovieSession.objects.get(id=session_id)

        if show_time:
            inst.show_time = show_time
        if movie_id:
            inst.movie_id = movie_id
        if cinema_hall_id:
            inst.cinema_hall_id = cinema_hall_id
        inst.save()


def delete_movie_session_by_id(session_id: int = None) -> None:
    if session_id:
        inst = MovieSession.objects.get(id=session_id)
        inst.delete()
