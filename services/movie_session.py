from db.models import MovieSession


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=cinema_hall_id,
        movie=movie_id
    )


def get_movies_sessions(session_date: MovieSession = None) -> MovieSession:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)

    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> int:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: MovieSession = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> MovieSession:
    get_session = MovieSession.objects.get(id=session_id)
    if show_time:
        get_session.show_time = show_time

    if movie_id:
        get_session.movie_id = movie_id

    if cinema_hall_id:
        get_session.cinema_hall_id = cinema_hall_id

    get_session.save()
    return get_session


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
