from db.models import MovieSession


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int,
) -> MovieSession:
    movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id,
    )
    return movie_session


def get_movies_sessions(
        session_date: str = None
) -> MovieSession:
    if session_date is not None:
        return MovieSession.objects.filter(
            show_time__date=session_date
        )
    return MovieSession.objects.all()


def get_movie_session_by_id(
        movie_session_id: int
) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    update_session = MovieSession.objects.get(
        id=session_id
    )
    if show_time is not None:
        update_session.show_time = show_time

    if movie_id is not None:
        update_session.movie_id = movie_id

    if cinema_hall_id is not None:
        update_session.cinema_hall_id = cinema_hall_id

    update_session.save()


def delete_movie_session_by_id(session_id):
    MovieSession.objects.filter(id=session_id).delete()
