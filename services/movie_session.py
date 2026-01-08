import datetime
from db.models import MovieSession, CinemaHall, Movie
from django.db.models import QuerySet


def create_movie_session(
        movie_show_time: datetime.datetime,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=CinemaHall.objects.get(id=cinema_hall_id),
        movie=Movie.objects.get(id=movie_id)
    )


def get_movies_sessions(
        session_date: str | None = None
) -> QuerySet:
    if session_date:
        date = datetime.datetime.strptime(session_date, "%Y-%m-%d")
        return MovieSession.objects.filter(
            show_time__date=date
        )
    return MovieSession.objects.all()


def get_movie_session_by_id(
        movie_session_id: int
) -> MovieSession:
    return MovieSession.objects.get(
        id=movie_session_id
    )


def update_movie_session(
        session_id: int,
        show_time: datetime.datetime | None = None,
        cinema_hall_id: int | None = None,
        movie_id: int | None = None
) -> None:
    session = MovieSession.objects.get(
        id=session_id
    )
    if show_time:
        session.show_time = show_time
    if cinema_hall_id:
        session.cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    if movie_id:
        session.movie = Movie.objects.get(id=movie_id)
    session.save()


def delete_movie_session_by_id(
        session_id: int,
) -> None:
    MovieSession.objects.get(
        id=session_id
    ).delete()
