from typing import List, Optional

from db.models import Movie, CinemaHall, MovieSession
from datetime import datetime


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    work_movie = Movie.objects.get(id=movie_id)
    work_cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    new_movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie=work_movie,
        cinema_hall=work_cinema_hall
    )
    return new_movie_session


def get_movies_sessions(
        session_date: Optional[str] = None
) -> List[MovieSession]:
    queryset = MovieSession.objects.all()
    if session_date is not None:
        date_format = "%Y-%m-%d"
        work_date = datetime.strptime(session_date, date_format)
        queryset = queryset.filter(show_time__date=work_date)

    return queryset


def get_movie_session_by_id(movie_session_id: MovieSession) -> Movie:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: Optional[datetime] = None,
        movie_id: Optional[int] = None,
        cinema_hall_id: Optional[int] = None
) -> None:
    update_movies_session = MovieSession.objects.filter(id=session_id)
    if show_time:
        update_movies_session.update(show_time=show_time,)
    if movie_id:
        update_movies_session.update(movie=movie_id)
    if cinema_hall_id:
        update_movies_session.update(cinema_hall=cinema_hall_id)


def delete_movie_session_by_id(session_id: MovieSession) -> None:
    delete_movies_session = MovieSession.objects.filter(id=session_id)
    delete_movies_session.delete()
