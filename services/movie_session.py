from datetime import datetime
from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> None:
    obj_movie = Movie.objects.get(id=movie_id)
    obj_cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)

    movie_session = MovieSession(show_time=movie_show_time,
                                 cinema_hall=obj_cinema_hall,
                                 movie=obj_movie)
    movie_session.save()


def get_movies_sessions(session_date: datetime = None) -> list[MovieSession]:
    movies_sessions = MovieSession.objects.all()
    if session_date:
        try:
            date_obj = datetime.strptime(session_date, "%Y-%m-%d").date()
            movies_sessions = movies_sessions.filter(show_time__date=date_obj)
        except ValueError:
            raise ValueError("session_date must be in 'YYYY-MM-DD' format")
    return movies_sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    try:
        return MovieSession.objects.get(id=movie_session_id)
    except MovieSession.DoesNotExist:
        return None


def update_movie_session(session_id: int,
                         show_time: datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> None:
    session = get_movie_session_by_id(session_id)
    if not session:
        return
    if show_time is not None:
        session.show_time = show_time
    if movie_id is not None:
        session.movie_id = movie_id
    if cinema_hall_id is not None:
        session.cinema_hall_id = cinema_hall_id
    session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    try:
        session = MovieSession.objects.get(id=session_id)
        session.delete()
    except MovieSession.DoesNotExist:
        pass
