import datetime

from django.db.models import QuerySet

from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(
        movie_show_time: datetime.datetime,
        cinema_hall_id: int,
        movie_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id

    )


def get_movies_sessions(
        session_date: str = None
) -> QuerySet | MovieSession:
    movie_sessions = MovieSession.objects.all()

    if session_date:
        date_obj = datetime.datetime.strptime(session_date, "%Y-%m-%d").date()
        return MovieSession.objects.filter(show_time__date=date_obj)
    return movie_sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime.datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> MovieSession:
    movie_session = MovieSession.objects.get(id=session_id)
    if show_time:
        movie_session.show_time = show_time
        movie_session.save()
    if movie_id:
        movie_session.movie_id = Movie.objects.get(id=movie_id)
        movie_session.save()
    if cinema_hall_id:
        movie_session.cinema_hall_id = CinemaHall.objects.get(
            id=cinema_hall_id
        )
        movie_session.save()
    return movie_session


def delete_movie_session_by_id(session_id: int) -> None:
    movie_session = MovieSession.objects.get(id=session_id)
    movie_session.delete()
