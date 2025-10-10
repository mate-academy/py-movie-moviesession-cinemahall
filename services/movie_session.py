from typing import List, Optional

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(movie_show_time, movie_id, cinema_hall_id) -> MovieSession:
     return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(session_date=None) -> QuerySet[MovieSession, MovieSession]:
    queryset = MovieSession.objects.all()
    if session_date:
        queryset = queryset.filter(
            show_time__date = session_date
        )
    return queryset


def get_movie_session_by_id(session_id) -> MovieSession:
    return MovieSession.objects.get(id=session_id)


def delete_movie_session_by_id(session_id) -> None:
    MovieSession.objects.filter(id=session_id).delete()

def update_movie_session(session_id, show_time=None, movie_id=None, cinema_hall_id=None) -> Optional[MovieSession]:
    try:
        session = get_movie_session_by_id(session_id)
    except MovieSession.DoesNotExist:
        return None

    if show_time is not None:
        session.show_time = show_time

    if movie_id is not None:
        session.movie_id = movie_id

    if cinema_hall_id is not None:
        session.cinema_hall_id = cinema_hall_id

    session.save()
    return session
