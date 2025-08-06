from django.db.models import QuerySet
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist

from services import movie, cinema_hall
from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    obj, created = MovieSession.objects.get_or_create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )
    return obj


def get_movies_sessions(session_date: str = None) -> QuerySet:
    if session_date:
        return MovieSession.objects.filter(
            show_time__date=datetime.strptime(session_date, "%Y-%m-%d").date()
        )
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession | None:
    try:
        return MovieSession.objects.get(id=movie_session_id)
    except ObjectDoesNotExist as e:
        print(e)
    except ValueError as e:
        print(e)
    return None


def update_movie_session(session_id: int,
                         show_time: datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None
                         ) -> MovieSession | None:
    movie_session = get_movie_session_by_id(movie_session_id=session_id)
    if movie_session:
        if show_time:
            movie_session.show_time = show_time
        if movie_id:
            movie_obj = movie.get_movie_by_id(movie_id)
            if movie_obj:
                movie_session.movie = movie_obj
        if cinema_hall_id:
            cinema_hall_obj = cinema_hall.get_cinema_halls_by_id(
                cinema_hall_id
            )
            if cinema_hall_obj:
                movie_session.cinema_hall = cinema_hall_obj
        if show_time or movie_id or cinema_hall_id:
            movie_session.save()
            return movie_session
    return None


def delete_movie_session_by_id(session_id: int) -> tuple | None:
    try:
        return MovieSession.objects.get(id=session_id).delete()
    except ObjectDoesNotExist as e:
        print(e)
    except ValueError as e:
        print(e)
    return None
