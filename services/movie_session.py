from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
        movie_show_time: str,
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
) -> QuerySet:
    queryset = MovieSession.objects.all()

    if session_date:
        queryset = queryset.filter(
            show_time__date=session_date
        )

    return queryset


def get_movie_session_by_id(
        movie_session_id: int
) -> MovieSession:
    return MovieSession.objects.get(
        id=movie_session_id
    )


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None,
) -> int:
    queryset = MovieSession.objects.filter(id=session_id)
    updated_entries_number = 0

    if queryset:
        if show_time:
            updated_entries_number += queryset.update(show_time=show_time)

        if movie_id:
            updated_entries_number += queryset.update(movie_id=movie_id)

        if cinema_hall_id:
            updated_entries_number += queryset.update(cinema_hall_id=cinema_hall_id)

    return updated_entries_number


def delete_movie_session_by_id(session_id: int) -> int:
    return MovieSession.objects.filter(id=session_id).delete()
