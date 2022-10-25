from datetime import datetime

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> MovieSession:
    new_movie_session = MovieSession(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )

    new_movie_session.save()

    return new_movie_session


def get_movies_sessions(session_date: str = None) -> QuerySet:
    if not session_date:
        return MovieSession.objects.all()

    desired_date = datetime.strptime(session_date, '%m-%d-%Y').date()

    return MovieSession.objects.filter(show_time__date=desired_date)


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> MovieSession:
    session_to_update = MovieSession.objects.get(id=session_id)

    if show_time:
        session_to_update.show_time = show_time
    if movie_id:
        session_to_update.movie_id = movie_id
    if cinema_hall_id:
        session_to_update.cinema_hall_id = cinema_hall_id

    return session_to_update


def delete_movie_session_by_id(movie_session_id: int) -> None:
    MovieSession.objects.get(id=movie_session_id).delete()
