from db.models import MovieSession, Movie, CinemaHall
from datetime import datetime
from typing import List, Optional


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    return MovieSession.objects.create(
        movie=movie,
        cinema_hall=cinema_hall,
        show_time=movie_show_time
    )


def get_movies_sessions(
        session_date: datetime = None
) -> Optional[List[MovieSession]]:
    qs = MovieSession.objects.all()
    if session_date:
        date_obj = datetime.strptime(session_date, "%Y-%m-%d").date()
        qs = qs.filter(show_time__date=date_obj)
    return qs


def get_movie_session_by_id(movie_session_id: int) -> Optional[MovieSession]:
    try:
        return MovieSession.objects.get(id=movie_session_id)
    except MovieSession.DoesNotExist:
        return None


def update_movie_session(session_id: int,
                         show_time: Optional[datetime] = None,
                         movie_id: Optional[int] = None,
                         cinema_hall_id: Optional[int] = None
                         ) -> Optional[MovieSession]:
    try:
        session = MovieSession.objects.get(id=session_id)
    except MovieSession.DoesNotExist:
        return None

    if show_time:
        session.show_time = show_time

    if movie_id:
        try:
            movie = Movie.objects.get(id=movie_id)
            session.movie = movie
        except Movie.DoesNotExist:
            pass

    if cinema_hall_id:
        try:
            hall = CinemaHall.objects.get(id=cinema_hall_id)
            session.cinema_hall = hall
        except CinemaHall.DoesNotExist:
            pass

    session.save()
    return session


def delete_movie_session_by_id(session_id: int) -> None:
            session = MovieSession.objects.filter(id=session_id)
            session.delete()
