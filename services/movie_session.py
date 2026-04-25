import datetime

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime.datetime,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movies_sessions(session_date: str = None) -> QuerySet[MovieSession]:
    query_set = MovieSession.objects.all()
    if session_date:
        session_date = datetime.datetime.strptime(
            session_date,
            "%Y-%m-%d"
        ).date()
        query_set = query_set.filter(show_time__date=session_date)
    return query_set


def get_movie_session_by_id(id_: int) -> MovieSession:
    return MovieSession.objects.get(id=id_)


def update_movie_session(
        session_id: int,
        show_time: datetime.datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    updated_movie_session = MovieSession.objects.get(id=session_id)
    if show_time:
        updated_movie_session.show_time = show_time
    if movie_id:
        updated_movie_session.movie_id = movie_id
    if cinema_hall_id:
        updated_movie_session.cinema_hall_id = cinema_hall_id
    updated_movie_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
