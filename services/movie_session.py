from django.db.models import QuerySet

from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(
    movie_show_time: str,
    movie_id: int,
    cinema_hall_id: int
) -> None:

    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)

    MovieSession.objects.create(
        show_time=movie_show_time,
        movie=movie,
        cinema_hall=cinema_hall
    )


def get_movies_sessions(session_date: str = None) -> QuerySet:
    if session_date is not None:
        return MovieSession.objects.filter(
            show_time__date=session_date
        )
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.filter(
        id=movie_session_id
    ).get()


def update_movie_session(
    session_id: int,
    show_time: str = None,
    movie_id: id = None,
    cinema_hall_id: id = None
) -> None:

    if show_time is not None:
        MovieSession.objects.filter(
            id=session_id
        ).update(show_time=show_time)

    if movie_id is not None:
        MovieSession.objects.filter(
            id=session_id
        ).update(movie_id=movie_id)

    if cinema_hall_id is not None:
        MovieSession.objects.update(
            cinema_hall_id=cinema_hall_id
        )


def delete_movie_session_by_id(session_id: int) -> None:
    get_movie_session_by_id(session_id).delete()
