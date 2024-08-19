from datetime import datetime

from django.db.models import QuerySet

from db.models import MovieSession, CinemaHall, Movie


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    cinema_hall = CinemaHall.objects.get(
        id=cinema_hall_id
    )
    movie = Movie.objects.get(
        id=movie_id
    )

    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=cinema_hall,
        movie=movie
    )


def get_movies_sessions(session_date: str = None) -> QuerySet:
    queryset = MovieSession.objects.all()
    if session_date:
        queryset = queryset.filter(
            show_time__date=session_date
        )
    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: Movie = None,
        cinema_hall_id: CinemaHall = None
) -> None:

    session = MovieSession.objects.get(id=session_id)
    if show_time:
        session.show_time = show_time
        session.save()
    if isinstance(movie_id, int):
        movie_inst = Movie.objects.get(id=movie_id)
        session.movie = movie_inst
        session.save()
    if isinstance(cinema_hall_id, int):
        cinema_hall_inst = CinemaHall.objects.get(id=cinema_hall_id)
        session.cinema_hall = cinema_hall_inst
        session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(
        id=session_id
    ).delete()
