from datetime import datetime

from django.db.models import QuerySet, F

from db.models import MovieSession


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> MovieSession:
    session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id)
    return session


def get_movies_sessions(session_date: str | None = None) -> QuerySet:
    # Беремо всі сесії та підвантажуємо пов'язані movie і cinema_hall
    queryset = MovieSession.objects.select_related(
        "movie",
        "cinema_hall"
    ).annotate(
        show_date=F('show_time__date')  # додаємо анотацію з тільки датою
    )

    # Фільтруємо по конкретній даті, якщо вказана
    if session_date:
        queryset = queryset.filter(show_time__date=session_date)

    # Сортуємо по даті, імені залу та назві фільму для детермінованого порядку
    queryset = queryset.order_by(
        "show_date",
        "cinema_hall__name",
        "movie__title"
    )

    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    session = MovieSession.objects.get(id=movie_session_id)
    return session


def update_movie_session(
        session_id: int,
        show_time: datetime | None = None,
        movie_id: int | None = None,
        cinema_hall_id: int | None = None) -> MovieSession:
    session = MovieSession.objects.get(id=session_id)
    if show_time:
        session.show_time = show_time
    if movie_id:
        session.movie_id = movie_id
    if cinema_hall_id:
        session.cinema_hall_id = cinema_hall_id
    session.save()
    return session


def delete_movie_session_by_id(session_id: int) -> None:
    session = MovieSession.objects.get(id=session_id)
    session.delete()
