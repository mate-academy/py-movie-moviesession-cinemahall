from db.models import MovieSession, Movie, CinemaHall

from django.db.models import QuerySet


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> None:

    get_movie = Movie.objects.get(id=movie_id)
    get_cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie=get_movie,
        cinema_hall=get_cinema_hall)
    movie_session.save()


def get_movies_sessions(session_date: str = None) -> QuerySet:
    movie_session = MovieSession.objects.all()
    if session_date:
        movie_session = MovieSession.objects.filter(
            show_time__date=session_date
        )
    return movie_session


def get_movie_session_by_id(movie_session_id: int) -> QuerySet:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:

    movie_session = MovieSession.objects.get(id=session_id)
    if show_time:
        movie_session.show_time = show_time
    if movie_id:
        movie_session.movie_id = movie_id
    if cinema_hall_id:
        movie_session.cinema_hall_id = cinema_hall_id
    movie_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
