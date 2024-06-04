import init_django_orm  # noqa: F401
import datetime

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
        movie_show_time: str,
        cinema_hall_id: int,
        movie_id: int
) -> MovieSession:
    movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )
    return movie_session


def get_movies_sessions(session_date: str = None) -> QuerySet | list:
    if session_date:
        queryset = MovieSession.objects.filter(show_time__date=session_date)
        return queryset

        # result = []
        # for movie_session in MovieSession.objects.all():
        #     if movie_session.show_time.strftime("%Y-%m-%d") == session_date:
        #         result.append(movie_session)
        # return result

    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> MovieSession:
    movie_session = MovieSession.objects.filter(id=session_id)
    if show_time:
        movie_session.update(show_time=show_time)
    if movie_id:
        movie_session.update(movie_id=movie_id)
    if cinema_hall_id:
        movie_session.update(cinema_hall_id=cinema_hall_id)
    return movie_session


def delete_movie_session_by_id(session_id: int) -> None:
    movie_session = MovieSession.objects.get(id=session_id)
    movie_session.delete()
