from db.models import Movie, MovieSession, CinemaHall
from datetime import datetime
from typing import Optional
from django.db.models import QuerySet



def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    movie = Movie.objects.get(id=movie_id)
    hall = CinemaHall.objects.get(id=cinema_hall_id)

    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie=movie,
        cinema_hall=hall
    )


def get_movies_sessions(
        session_date: Optional[str] = None
) -> QuerySet[MovieSession]:
    queryset = MovieSession.objects.all()

    if session_date:
        datetime_object = datetime.strptime(session_date, "%Y-%m-%d")
        queryset = queryset.filter(show_time__date=datetime_object.date())

    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time : Optional[datetime] = None,
        movie_id: Optional[int] = None,
        cinema_hall_id: Optional[int] = None
) -> MovieSession:
    session = MovieSession.objects.get(id=session_id)

    if show_time:
        session.show_time = show_time
    if movie_id:
        session.movie_id = movie_id
    if cinema_hall_id:
        session.cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)

    session.save()
    return session


def delete_movie_session_by_id(session_id: int) -> None:
    session = MovieSession.objects.get(id=session_id)
    session.delete()
