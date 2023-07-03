from db.models import MovieSession, CinemaHall, Movie


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=CinemaHall(id=cinema_hall_id),
        movie=Movie(id=movie_id)
    )


def get_movies_sessions(session_date: str = None) -> MovieSession:
    sessions = MovieSession.objects.all()

    if session_date:
        sessions = sessions.filter(show_time__date=session_date)

    return sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None,
) -> None:
    session = get_movie_session_by_id(session_id)

    if show_time:
        session.show_time = show_time

    if movie_id:
        session.movie = Movie(id=movie_id)

    if cinema_hall_id:
        session.cinema_hall = CinemaHall(id=cinema_hall_id)

    session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    session = MovieSession.objects.get(id=session_id)
    session.delete()
