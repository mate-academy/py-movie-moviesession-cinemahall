from datetime import datetime

from django.db.models import QuerySet

from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    return MovieSession.object.create(
        cinema_hall=cinema_hall_id,
        movie=Movie.objects.get(movie_id),
        show_time=CinemaHall.objects.get(movie_show_time)
    )


def get_movies_sessions(
    session_date: str = None,
) -> QuerySet:
    current_session = MovieSession.objects.all()

    if session_date:
        session_date = datetime.strptime(session_date, "%y-%m-%d").date()
        current_session = current_session.filter(
            show_time__date=session_date
        )

    return current_session


def get_movie_session_by_id(
        movie_session_id: int
) -> QuerySet:
    return MovieSession.objects.filter(
        id=movie_session_id
    )


def update_movie_session(
        session_id: int,
        show_time: datetime.date = None,
        movie_id: int = None,
        cinema_hall_id: int = None,

) -> None:
    movie_session = MovieSession.objects.get(
        id=session_id
    )

    if show_time:
        movie_session.show_time = show_time

    if movie_id:
        movie_session.movie = Movie.objects.get(
            id=movie_id
        )

    if cinema_hall_id:
        movie_session.cinema_hall = CinemaHall.objects.get(
            id=cinema_hall_id
        )

    movie_session.save()


def delete_movie_session_by_id(
        session_id: int
) -> None:
    MovieSession.objects.get(
        id=session_id
    ).delete()
