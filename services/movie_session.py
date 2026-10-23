from django.db.models import QuerySet
from db.models import MovieSession, CinemaHall, Movie


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    movie = Movie.objects.get(id=movie_id)
    cinemahall = CinemaHall.objects.get(id=cinema_hall_id)
    moviesession = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=cinemahall,
        movie=movie,
    )
    return moviesession


def get_movies_sessions(session_date: str | None = None) -> QuerySet:
    if session_date:
        return MovieSession.objects.filter(
            show_time__date=session_date
        )
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(
        id=movie_session_id
    )


def update_movie_session(
        session_id: int,
        show_time: str | None = None,
        movie_id: int | None = None,
        cinema_hall_id: int | None = None
) -> None:
    moviesession = MovieSession.objects.get(
        id=session_id
    )
    if show_time:
        moviesession.show_time = show_time
    if movie_id:
        movie = Movie.objects.get(id=movie_id)
        moviesession.movie = movie
    if cinema_hall_id:
        cinemahall = CinemaHall.objects.get(id=cinema_hall_id)
        moviesession.cinema_hall = cinemahall
    moviesession.save()


def delete_movie_session_by_id(session_id: int) -> None:
    moviesession = MovieSession.objects.get(
        id=session_id
    )
    moviesession.delete()
