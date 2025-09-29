import datetime

from django.db.models import QuerySet

from db.models import MovieSession, CinemaHall, Movie


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
    session_date: str = None
) -> QuerySet[MovieSession]:
    result = MovieSession.objects.all()
    if session_date:
        result = result.filter(
            show_time__date=datetime.datetime.strptime(
                session_date, "%Y-%m-%d"
            )
        )
    return result


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
    session_id: int,
    show_time: datetime.datetime = None,
    movie_id: int = None,
    cinema_hall_id: int = None
) -> None:
    session = get_movie_session_by_id(session_id)
    if show_time and isinstance(show_time, datetime.datetime):
        session.show_time = show_time
    if movie_id and (movie := Movie.objects.filter(id=movie_id).first()):
        session.movie = movie
    if cinema_hall_id and (
        hall := CinemaHall.objects.filter(id=cinema_hall_id).first()
    ):
        session.cinema_hall = hall
    session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
