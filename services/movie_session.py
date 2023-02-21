from datetime import datetime
from db.models import MovieSession, Movie, CinemaHall
from django.db.models.query import QuerySet


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=CinemaHall.objects.get(id=cinema_hall_id),
        movie=Movie.objects.get(id=movie_id)
    )

    return movie_session


def get_movies_sessions(session_date: str = None) -> QuerySet:
    queryset = MovieSession.objects.all()

    if session_date:
        year, month, day = session_date.split("-")
        queryset = queryset.filter(
            show_time__date=datetime(
                year=int(year),
                month=int(month),
                day=int(day)
            )
        )

    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    movie_session = MovieSession.objects.filter(id=session_id)

    if show_time:
        movie_session.update(show_time=show_time)

    if movie_id:
        movie_session.update(movie=Movie.objects.get(id=movie_id))

    if cinema_hall_id:
        movie_session.update(
            cinema_hall=CinemaHall.objects.get(id=cinema_hall_id)
        )


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
