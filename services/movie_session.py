from datetime import datetime
from db.models import MovieSession
from django.db.models import QuerySet


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> MovieSession:
    return MovieSession.objects.create(movie_id=movie_id,
                                       cinema_hall_id=cinema_hall_id,
                                       show_time=movie_show_time)


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def delete_movie_session_by_id(session_id: int) -> tuple[int, dict]:
    return MovieSession.objects.filter(id=session_id).delete()


def update_movie_session(session_id: int,
                         show_time: datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> bool:
    try:
        movie_session = MovieSession.objects.get(id=session_id)
        if show_time:
            movie_session.show_time = show_time
        if movie_id:
            movie_session.movie_id = movie_id
        if cinema_hall_id:
            movie_session.cinema_hall_id = cinema_hall_id
        movie_session.save()
    except MovieSession.DoesNotExist:
        raise ValueError("Сеанс фільму з таким id не знайдений.")


def get_movies_sessions(session_date: datetime = None) \
        -> QuerySet(MovieSession):
    if session_date is not None:
        if isinstance(session_date, str):  # Check if it's a string
            session_date = datetime.strptime(session_date, "%Y-%m-%d")

        # Now that session_date is a datetime object, get its date part
        norm_date = session_date.date()
        return MovieSession.objects.filter(show_time__date=norm_date)
    else:
        return MovieSession.objects.all()
