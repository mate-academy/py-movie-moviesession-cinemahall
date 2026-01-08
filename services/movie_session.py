import datetime
from django.db.models import QuerySet
from db.models import MovieSession


def create_movie_session(movie_show_time: datetime.datetime, movie_id: int,
                         cinema_hall_id: int) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(session_date: str = None) -> QuerySet:
    if not session_date:
        return MovieSession.objects.all()

    try:
        session_date = datetime.datetime.strptime(session_date,
                                                  "%Y-%m-%d").date()
        return MovieSession.objects.filter(show_time__date=session_date)
    except ValueError:
        raise ValueError(
            "Invalid date format. Expected format: 'year-month-day'")


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: str | datetime.datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> None:
    # Проверка и преобразование строки show_time в datetime
    if show_time and isinstance(show_time, str):
        try:
            show_time = datetime.datetime.strptime(show_time, "%Y-%m-%d")
        except ValueError:
            raise ValueError(
                "Invalid date format. Expected format: 'year-month-day'"
            )

    # Формирование словаря обновляемых данных
    update_data = {}
    if show_time:
        update_data["show_time"] = show_time
    if movie_id is not None:
        update_data["movie_id"] = movie_id
    if cinema_hall_id is not None:
        update_data["cinema_hall_id"] = cinema_hall_id

    # Проверка, что есть данные для обновления
    if not update_data:
        raise ValueError("No fields to update were provided.")

    # Обновление записи
    MovieSession.objects.filter(id=session_id).update(**update_data)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
