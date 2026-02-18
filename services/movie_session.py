from django.db.models import QuerySet
from datetime import datetime

from db.models import MovieSession, CinemaHall, Movie


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    movie = Movie.objects.get(id=movie_id)

    MovieSession.objects.create(
        show_time=movie_show_time,
        movie=movie,
        cinema_hall=cinema_hall
    )


def get_movies_sessions(
        session_date: str | None = None
) -> QuerySet[MovieSession]:
    query_set = MovieSession.objects.all()

    if session_date:
        try:
            formatted_time = datetime.strptime(session_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError(
                f"Wrong value {session_date}. "
                f"Expected YYYY-MM-DD"
            )
        query_set = query_set.filter(show_time__date=formatted_time.date())

    return query_set


def get_movie_session_by_id(
        movie_session_id: int
) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    movie_session = MovieSession.objects.get(id=session_id)

    if movie_session is not None:
        if show_time is not None:
            show_time = datetime.strftime(show_time, "%Y-%m-%d")
            movie_session.show_time = show_time

        if cinema_hall_id is not None:
            movie_session.cinema_hall_id = cinema_hall_id

        if movie_id is not None:
            movie_session.movie_id = movie_id
        movie_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
