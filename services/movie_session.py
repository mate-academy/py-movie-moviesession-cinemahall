from db.models import MovieSession


def create_movie_session(
        movie_show_time: int,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )
    return movie_session


def get_movies_sessions(session_date: str | None = None) -> MovieSession:
    all_sessions = MovieSession.objects.all()

    if session_date is not None:
        all_sessions = all_sessions.filter(show_time__date=session_date)
    return all_sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    session_ids = MovieSession.objects.get(id=movie_session_id)
    return session_ids


def update_movie_session(
        session_id: int,
        show_time: str | None = None,
        movie_id: int | None = None,
        cinema_hall_id: int | None = None
) -> MovieSession:
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
    return update_session


def delete_movie_session_by_id(session_id: int) -> None:
    del_session = MovieSession.objects.filter(id=session_id)
    return del_session.delete()
