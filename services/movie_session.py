import init_django_orm  # noqa: F401

from db.models import MovieSession


def create_movie_session(
        movie_show_time: object, movie_id: int = None,
        cinema_hall_id: int = None) -> object:
    """
    Create new movie session
    """
    new_movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id, movie_id=movie_id
    )

    return new_movie_session


def get_movies_sessions(session_date: str = None) -> object:
    """
    Retrieve list movie sessions by filter date ("year-month-day")
    """
    queryset = MovieSession.objects.all()

    if session_date is not None:
        queryset = queryset.filter(show_time__date=session_date)

    return queryset


def get_movie_session_by_id(movie_session_id : int) -> object:
    """
    Retrieve movie session by movie_session_id
    """
    movie_session = MovieSession.objects.get(id=movie_session_id)

    return movie_session


def update_movie_session(
        session_id: int, show_time: object = None,
        movie_id: int = None, cinema_hall_id: int = None) -> object:
    update_param = {}

    if show_time is not None:
        update_param["show_time"] = show_time

    if movie_id is not None:
        update_param["movie"] = movie_id

    if cinema_hall_id is not None:
        update_param["cinema_hall"] = cinema_hall_id

    if len(update_param):
        MovieSession.objects.filter(
            id=session_id
        ).update(**update_param)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(
        id=session_id
    ).delete()
