from django.db.models import QuerySet

from datetime import datetime, date

from db.models import MovieSession


def create_movie_session(
        movie_show_time: date,
        movie_id: int,
        cinema_hall_id: int,
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id,
    )


def get_movies_sessions(
    session_date: str = None
) -> QuerySet[MovieSession]:
    queryset = MovieSession.objects.all()
    if session_date:
        date_obj = datetime.strptime(session_date, "%Y-%m-%d")
        return queryset.filter(session_date=date_obj)
    else:
        return queryset


def update_movie_session(
        session_id: int,
        show_time: None,
        movie_id: int = None,
        cinema_hall_id: int = None,
) -> MovieSession:
    movie_session = MovieSession.objects.get(id=session_id)
    if show_time:
        movie_session.show_time = show_time
    if movie_id:
        movie_session.movie_id = movie_id
    if cinema_hall_id:
        movie_session.cinema_hall_id = cinema_hall_id

    movie_session.save()
    return movie_session


def delete_movie_session_by_id(session_id: int) -> None:
    return MovieSession.objects.filter(id=session_id).delete()
