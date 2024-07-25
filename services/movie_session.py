from datetime import datetime

from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:

    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)

    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=cinema_hall,
        movie=movie,
    )


def get_movies_sessions(session_date: str = None) -> MovieSession:
    sessions = MovieSession.objects.all()
    if session_date:
        date_to_find = datetime.strptime(session_date, "%Y-%m-%d")
        sessions = sessions.filter(show_time__date=date_to_find.date())
    return sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        cinema_hall_id: int = None,
        movie_id: int = None,

) -> None:
    movie_session = MovieSession.objects.filter(id=session_id)

    if show_time:
        movie_session.update(show_time=show_time)
    if cinema_hall_id:
        movie_session.update(cinema_hall=cinema_hall_id)
    if movie_id:
        movie_session.update(movie=movie_id)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
