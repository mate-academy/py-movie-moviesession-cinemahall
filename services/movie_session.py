from datetime import datetime, date

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int
                         ) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def get_movies_sessions(session_date: str = None) -> QuerySet:
    if session_date:
        sess_date_sp = session_date.split("-")
        sess_date = date(int(sess_date_sp[0]),
                         int(sess_date_sp[1]),
                         int(sess_date_sp[2]))
        return MovieSession.objects.filter(show_time__date=sess_date)
    return MovieSession.objects.all()


def update_movie_session(session_id: int,
                         show_time: datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> None:
    movie_session_instance = MovieSession.objects.get(id=session_id)
    if show_time:
        movie_session_instance.show_time = show_time
    if movie_id:
        movie_session_instance.movie_id = movie_id
    if cinema_hall_id:
        movie_session_instance.cinema_hall_id = cinema_hall_id
    movie_session_instance.save()


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
