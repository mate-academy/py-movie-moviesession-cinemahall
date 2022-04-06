from datetime import datetime
from typing import List

from db.models import MovieSession


# Create Movies Sessions
def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
):
    MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


# Retrieve Movie Sessions
def get_movies_sessions(session_date: str = None) -> List[object]:
    queryset = MovieSession.objects.all()

    if session_date:
        return queryset.filter(show_time__date=session_date)
    return queryset


# Retrieve Movie Session by id
def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(
        movie_id=movie_session_id
    )


# Update Movie Session
def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
):
    update_movie_session_ = MovieSession.objects.filter(
        id=session_id
    )

    if show_time:
        update_movie_session_.update(show_time=show_time)

    if movie_id:
        update_movie_session_.update(movie_id=movie_id)

    if cinema_hall_id:
        update_movie_session_.update(cinema_hall_id=cinema_hall_id)


# Delete Movie Session
def delete_movie_session_by_id(session_id: int):
    MovieSession.objects.filter(id=session_id).delete()
