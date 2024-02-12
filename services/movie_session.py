from datetime import datetime

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movies_sessions(session_date: str = None) -> QuerySet:
    queryset = MovieSession.objects.all()

    if session_date:
        start_datetime = datetime.strptime(
            session_date + " 00:00:00",
            "%Y-%m-%d %H:%M:%S")
        end_datetime = datetime.strptime(
            session_date + " 23:59:59",
            "%Y-%m-%d %H:%M:%S")

        queryset = queryset.filter(
            show_time__range=(start_datetime, end_datetime)
        )

    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> MovieSession:
    movie_session = MovieSession.objects.get(id=session_id)
    if show_time:
        movie_session.show_time = show_time
    if movie_id:
        movie_session.movie_id = movie_id
    if cinema_hall_id:
        movie_session.cinema_hall_id = cinema_hall_id

    return movie_session.save()


def delete_movie_session_by_id(session_id: int) -> MovieSession:
    return get_movie_session_by_id(session_id).delete()
