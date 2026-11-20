from datetime import datetime
from db.models import MovieSession


def create_movie_session(
    movie_show_time: datetime,
    movie_id: int,
    cinema_hall_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions():
    pass


def get_movie_session_by_id():
    pass


def update_movie_session():
    pass


def delete_movie_session_by_id():
    pass
