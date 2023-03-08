import datetime

from django.db.models import QuerySet

from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(
        movie_show_time: datetime.datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:

    get_movie_id = Movie.objects.get(id=movie_id)
    get_cinema_id = CinemaHall.objects.get(id=cinema_hall_id)
    movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=get_cinema_id,
        movie=get_movie_id
    )
    return movie_session


def get_movies_sessions(session_date: str = None) -> QuerySet[MovieSession]:
    all_movies = MovieSession.objects.all()

    if session_date is not None:
        filtered_movies = MovieSession.objects.filter(
            show_time__date=session_date
        )
        return filtered_movies
    return all_movies


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    movie_session = MovieSession.objects.get(id=movie_session_id)
    return movie_session


def update_movie_session(
        session_id: int,
        show_time: datetime.datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    movie = MovieSession.objects.get(id=session_id)

    if show_time is not None:
        movie.show_time = show_time

    if movie_id is not None:
        movie.movie_id = movie_id

    if cinema_hall_id is not None:
        movie.cinema_hall_id = cinema_hall_id

    movie.save()
    return


def delete_movie_session_by_id(session_id: int) -> None:
    deleted_movie_session = MovieSession.objects.get(id=session_id)
    deleted_movie_session.delete()
