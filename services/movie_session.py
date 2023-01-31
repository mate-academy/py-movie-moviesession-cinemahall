from django.db.models import QuerySet

from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(movie_show_time: int,
                         movie_id: int,
                         cinema_hall_id: int) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        movie=Movie.objects.get(id=movie_id),
        cinema_hall=CinemaHall.objects.get(id=cinema_hall_id)
    )


def get_movies_sessions(session_date: str = None) -> QuerySet:
    movie_sessions = MovieSession.objects.all()
    if session_date:
        movie_sessions = movie_sessions.filter(
            show_time__date=session_date
        )
    return movie_sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession | list:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: str = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> None:
    movie_session = MovieSession.objects.filter(id=session_id)
    if show_time:
        movie_session.update(
            show_time=show_time
        )
    if movie_id:
        movie_session.update(
            movie_id=movie_id
        )
    if cinema_hall_id:
        movie_session.update(
            cinema_hall_id=cinema_hall_id
        )


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
