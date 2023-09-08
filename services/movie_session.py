from django.db.models import QuerySet

from db.models import MovieSession

import datetime


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:

    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(session_date: str = None) -> QuerySet:
    queryset = MovieSession.objects.all()

    if session_date:
        date_ls = [int(period) for period in session_date.split("-")]
        queryset = queryset.filter(
            show_time__date=datetime.date(date_ls[0], date_ls[1], date_ls[2]),
        )

    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> int:
    movie_session = get_movie_session_by_id(session_id)
    changes_count = 0

    if show_time:
        movie_session.show_time = show_time
        movie_session.save()
        changes_count += 1

    if movie_id:
        movie_session.movie_id = movie_id
        movie_session.save()
        changes_count += 1

    if cinema_hall_id:
        movie_session.cinema_hall_id = cinema_hall_id
        movie_session.save()
        changes_count += 1

    return changes_count


def delete_movie_session_by_id(movie_session_id: int) -> None:
    get_movie_session_by_id(movie_session_id).delete()
