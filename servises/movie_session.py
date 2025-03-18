from db.models import MovieSession


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    return MovieSession(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id,
    )


def get_movie_session(session_date: str = None) -> MovieSession:
    if session_date:
        return MovieSession.objects.filter(
            show_time=session_date
        )
    else:
        return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(movie_id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None,
) -> None:
    movie_session = get_movie_session_by_id(session_id)

    if show_time:
        movie_session.objects.update(
            show_time=show_time
        )

    if movie_id:
        movie_session.objects.update(
            movie_id=movie_id
        )

    if cinema_hall_id:
        movie_session.objects.update(
            cinema_hall_id=cinema_hall_id
        )


def delete_movie_session(session_id: int) -> None:
    movie_session = get_movie_session_by_id(session_id)
    movie_session.delete()
