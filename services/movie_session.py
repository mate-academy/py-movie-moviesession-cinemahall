from django.db.models import QuerySet
from django.utils.dateparse import parse_date
from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(movie_show_time: str, movie_id: int,
                         cinema_hall_id: int) -> MovieSession:
    movie_session = MovieSession(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id)
    movie_session.save()
    return movie_session


def get_movies_sessions(
        session_date: str | None = None) -> QuerySet[MovieSession]:
    if session_date:
        parsed_date = parse_date(session_date)
        return MovieSession.objects.filter(show_time__date=parsed_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: str | None = None,
                         movie_id: int | None = None,
                         cinema_hall_id: int | None = None) -> None:
    movie_session = MovieSession.objects.get(id=session_id)
    if show_time:
        movie_session.show_time = show_time
    if movie_id:
        movie_session.movie = Movie.objects.get(id=movie_id)
    if cinema_hall_id:
        movie_session.cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    movie_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    movie_session = MovieSession.objects.get(id=session_id)
    movie_session.delete()
