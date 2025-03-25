from typing import Optional
from datetime import datetime
from django.db.models import QuerySet
from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> Optional[MovieSession]:
    movie = Movie.objects.filter(id=movie_id).first()
    cinema_hall = CinemaHall.objects.filter(id=cinema_hall_id).first()

    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie=movie,
        cinema_hall=cinema_hall
    )


def get_movies_sessions(session_date: Optional[str] = None) -> QuerySet:
    sessions = MovieSession.objects.all()
    if session_date:
        sessions = sessions.filter(show_time__date=session_date)
    return sessions


def get_movie_session_by_id(movie_session_id: int) -> Optional[MovieSession]:
    return MovieSession.objects.filter(id=movie_session_id).first()


def update_movie_session(session_id: int,
                         show_time: Optional[datetime] = None,
                         movie_id: Optional[int] = None,
                         cinema_hall_id: Optional[int] = None
                         ) -> Optional[MovieSession]:
    session = MovieSession.objects.filter(id=session_id).first()
    if not session:
        return None

    update_data = {}
    if show_time:
        update_data["show_time"] = show_time
    if movie_id:
        update_data["movie"] = Movie.objects.filter(id=movie_id).first()
    if cinema_hall_id:
        update_data["cinema_hall"] = CinemaHall.objects.filter(
            id=cinema_hall_id).first()

    if update_data:
        MovieSession.objects.filter(id=session_id).update(**update_data)

    return MovieSession.objects.get(id=session_id)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
