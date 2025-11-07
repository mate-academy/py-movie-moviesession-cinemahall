from datetime import datetime
from django.db.models import QuerySet
from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)

    session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie=movie,
        cinema_hall=cinema_hall
    )
    return session


def get_movies_sessions(session_date: str = None) -> QuerySet[MovieSession]:
    sessions = MovieSession.objects.all()
    if session_date:
        try:
            date_obj = datetime.strptime(session_date, "%Y-%m-%d").date()
            sessions = sessions.filter(show_time__date=date_obj)
        except ValueError:
            # якщо рядок не відповідає формату, повертаємо порожній queryset
            return MovieSession.objects.none()
    return sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession | None:
    return MovieSession.objects.filter(id=movie_session_id).first()


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> MovieSession | None:

    session = MovieSession.objects.filter(id=session_id).first()
    if not session:
        return None

    if show_time is not None:
        session.show_time = show_time
    if movie_id is not None:
        session.movie_id = movie_id
    if cinema_hall_id is not None:
        session.cinema_hall_id = cinema_hall_id

    session.save()
    return session


def delete_movie_session_by_id(session_id: int) -> bool:
    session = MovieSession.objects.filter(id=session_id).first()
    if not session:
        return False
    session.delete()
    return True
