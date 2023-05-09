from db.models import MovieSession

import datetime


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie=movie_id,
        cinema_hall=cinema_hall_id
    )

    return movie_session


def get_movie_sessions(
        session_date: datetime
) -> MovieSession:
    return MovieSession.objects.all().filter(
        show_time__date=session_date
    )


def get_movie_session_by_id(
        movie_session_id: int
) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    MovieSession.objects.filter(
        id=session_id
    ).update(
        show_time=show_time,
        movie=movie_id,
        cinema_hall=cinema_hall_id
    )


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
