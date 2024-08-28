from datetime import datetime

from django.db.models import QuerySet

from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int,
) -> MovieSession:
    new_movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=CinemaHall.objects.get(id=cinema_hall_id),
        movie=Movie.objects.get(id=movie_id)
    )
    return new_movie_session


def get_movies_sessions(session_date: str = None) -> QuerySet:
    if session_date:
        target_time = datetime.strptime(session_date, "%Y-%m-%d").date()
        return MovieSession.objects.filter(show_time__date=target_time)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    movie_session = MovieSession.objects.get(id=session_id)

    if show_time:
        movie_session.show_time = show_time

    if cinema_hall_id:
        cinema_hall_inst = CinemaHall.objects.filter(id=cinema_hall_id)
        if cinema_hall_inst.exists():
            movie_session.cinema_hall = cinema_hall_inst.first()

    if movie_id:
        movie_inst = Movie.objects.filter(id=movie_id)
        if movie_inst.exists():
            movie_session.movie = movie_inst.first()

    movie_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
