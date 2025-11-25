from db.models import MovieSession


def create_movie_session(
        movie_show_time: int,
        movie_id: str,
        cinema_hall_id: int
) -> MovieSession:
    session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )
    return session


def get_movies_sessions(session_date: int = None) -> MovieSession:

    if session_date is None:
        return MovieSession.objects.all()
    return MovieSession.objects.filter(show_time__date=session_date)


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: int = None,
        movie_id: str = None,
        cinema_hall_id: int = None
) -> MovieSession:
    session = MovieSession.objects.get(id=session_id)

    if show_time is not None:
        session.show_time = show_time
    if movie_id is not None:
        session.movie_id = movie_id
    if cinema_hall_id is not None:
        session.cinema_hall_id = cinema_hall_id

    session.save()
    return session


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
