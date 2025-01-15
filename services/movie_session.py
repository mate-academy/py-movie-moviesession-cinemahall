from datetime import datetime

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(movie_show_time: datetime, movie_id: int,
                         cinema_hall_id: int) -> QuerySet | MovieSession:
    new_movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id,
    )

    return new_movie_session


def get_movies_sessions(session_date: str = None) -> QuerySet | MovieSession:
    if session_date:
        session_date_obj = datetime.strptime(session_date, "%Y-%m-%d")
        movie_sessions = MovieSession.objects.filter(
            show_time__date=session_date_obj.date()
        )
    else:
        return MovieSession.objects.all()

    return movie_sessions


def get_movie_session_by_id(movie_session_id: int) -> QuerySet | MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int, show_time: datetime = None,
                         movie_id: int = None, cinema_hall_id: int = None)\
        -> QuerySet | MovieSession:
    updated_movie_session = MovieSession.objects.get(id=session_id)

    if movie_id:
        updated_movie_session.movie_id = movie_id
        updated_movie_session.save()
    if cinema_hall_id:
        updated_movie_session.cinema_hall_id = cinema_hall_id
        updated_movie_session.save()
    if show_time:
        updated_movie_session.show_time = show_time
        updated_movie_session.save()

    return updated_movie_session


def delete_movie_session_by_id(session_id: int) -> QuerySet | MovieSession:
    MovieSession.objects.filter(id=session_id).delete()
