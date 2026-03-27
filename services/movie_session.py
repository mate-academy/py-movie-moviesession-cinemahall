from datetime import datetime

from typing import Optional

from django.db.models import QuerySet

from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession | None:
    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)

    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie=movie,
        cinema_hall=cinema_hall
    )


def get_movies_sessions(
        session_date: Optional[str] = None
) -> QuerySet[MovieSession]:
    queryset = MovieSession.objects.all()

    if session_date:
        queryset = queryset.filter(show_time__date=session_date)

    return queryset


def get_movie_session_by_id(
        movie_session_id: int
) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> MovieSession | None:
    if session_id is not None:
        update_movie_session = MovieSession.objects.get(id=session_id)
        if show_time is not None:
            update_movie_session.show_time = show_time
        if movie_id is not None:
            update_movie_session.movie = Movie.objects.get(id=movie_id)
        if cinema_hall_id is not None:
            update_movie_session.cinema_hall = CinemaHall.objects.get(
                id=cinema_hall_id
            )

        update_movie_session.save()
        return update_movie_session
    return None


def delete_movie_session_by_id(session_id: int) -> bool:
    MovieSession.objects.get(id=session_id).delete()
    return True
