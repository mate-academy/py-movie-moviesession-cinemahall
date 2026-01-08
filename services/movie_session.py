from datetime import datetime

from db.models import MovieSession, CinemaHall, Movie


def create_movie_session(
        movie_show_time: str, movie_id: int, cinema_hall_id: int
) -> MovieSession:
    new_session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=CinemaHall(id=cinema_hall_id),
        movie=Movie(id=movie_id)
    )

    return new_session


def get_movies_sessions(session_date: str = None) -> MovieSession:
    queryset = MovieSession.objects.all()

    if session_date is not None:
        date_session = datetime.strptime(session_date, "%Y-%m-%d").date()
        queryset = queryset.filter(show_time__date=date_session)
    return queryset.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession | None:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None,
) -> None:
    fields_to_update = {}

    if show_time is not None:
        fields_to_update["show_time"] = show_time

    if movie_id is not None:
        fields_to_update["movie_id"] = movie_id

    if cinema_hall_id is not None:
        fields_to_update["cinema_hall_id"] = cinema_hall_id

    MovieSession.objects.filter(id=session_id).update(**fields_to_update)


def delete_movie_session_by_id(session_id: int) -> None:
    get_movie_session_by_id(session_id).delete()
