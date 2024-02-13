from db.models import MovieSession

import datetime


def create_movie_session(
        movie_show_time,
        movie_id: int,
        cinema_hall_id: int
):
    MovieSession.objects.create(
        show_time=movie_show_time,
        movie=movie_id,
        cinema_hall=cinema_hall_id
    )


def get_movie_sessions(session_date: str = None):
    if session_date:
        return MovieSession.objects.filter(
            show_time=datetime.datetime(*session_date.split("-"))
        )
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_id: int):
    return MovieSession.objects.get(movie_id=movie_id)


def update_movie_session(
        session_id: int,
        /,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None
):
    if show_time:
        MovieSession.objects.filter(
            id=session_id
        ).update(
            show_time=datetime.datetime(*show_time.split("-"))
        )
    if movie_id:
        MovieSession.objects.filter(
            id=session_id
        ).update(
            movie_id=movie_id
        )
    if cinema_hall_id:
        MovieSession.objects.filter(
            id=session_id
        ).update(
            cinema_hall_id=cinema_hall_id
        )


def delete_movie_session(session_id: int):
    MovieSession.objects.get(id=session_id).delete()
