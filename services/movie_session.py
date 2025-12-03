from datetime import datetime

from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(movie_show_time: datetime,
                         movie_id: int, cinema_hall_id: int) -> MovieSession:
    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    new_session = MovieSession(
        show_time=movie_show_time,
        cinema_hall=cinema_hall,
        movie=movie
    )
    new_session.save()
    return new_session


def get_movies_sessions(session_date: str = None) -> MovieSession:
    if session_date is None:
        return MovieSession.objects.all()
    else:
        new_date = datetime.strptime(session_date,
                                     "%Y-%m-%d").date()
        return MovieSession.objects.filter(show_time__date = new_date)


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: datetime=None,
                         movie_id: int=None,
                         cinema_hall_id: int=None) -> MovieSession:
    session = MovieSession.objects.get(id = session_id)
    if show_time:
        session.show_time = show_time
    if movie_id:
        session.movie = Movie.objects.get(id = movie_id)
    if cinema_hall_id:
        session.cinema_hall = CinemaHall.objects.get(id = cinema_hall_id)

    session.save()
    return session


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id = session_id).delete()