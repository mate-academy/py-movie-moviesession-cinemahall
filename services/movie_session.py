from db.models import MovieSession


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movies_sessions(
        session_date: str = None
) -> MovieSession:
    movie_sessions_in_this_date = MovieSession.objects.all()
    if session_date is not None:
        movie_sessions_in_this_date = movie_sessions_in_this_date.filter(
            show_time__date=session_date
        )
    print(session_date)
    return movie_sessions_in_this_date


def get_movie_session_by_id(
    movie_session_id: int
) -> MovieSession:
    return MovieSession.objects.filter(
        movie__id=movie_session_id
    )


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    movie_sessions = MovieSession.objects.filter(id=session_id)
    print(movie_sessions)
    if show_time is not None:
        movie_sessions.update(show_time=show_time)
    if movie_id is not None:
        movie_sessions.update(movie_id=movie_id)
    if cinema_hall_id is not None:
        movie_sessions.update(cinema_hall_id=cinema_hall_id)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
