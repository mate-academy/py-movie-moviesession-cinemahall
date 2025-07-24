from django.db.models import QuerySet

from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:

    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)

    new_movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie=movie,
        cinema_hall=cinema_hall
    )

    return new_movie_session


def get_movies_sessions(session_date: str = None) -> QuerySet:

    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> MovieSession:

    update_movie = MovieSession.objects.get(id=session_id)
    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)

    if show_time:
        update_movie.show_time = show_time

    if movie_id:
        update_movie.movie = movie

    if cinema_hall_id:
        update_movie.cinema_hall = cinema_hall

    update_movie.save()

    return update_movie


def delete_movie_session_by_id(session_id: int) -> None:
    delete_session = MovieSession.objects.get(id=session_id)
    delete_session.delete()
