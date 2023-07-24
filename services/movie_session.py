from db.models import MovieSession, CinemaHall


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:

    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    movi_session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=cinema_hall,
        movie_id=movie_id
    )

    return movi_session


def get_movies_sessions(
        session_date: str = None
) -> MovieSession:

    movies_sessions = MovieSession.objects.all()

    if session_date:
        movies_sessions = movies_sessions.filter(show_time__date=session_date)

    return movies_sessions


def get_movie_session_by_id(
        movie_session_id: int
) -> MovieSession:

    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> MovieSession:

    updater = MovieSession.objects.get(id=session_id)

    if show_time:
        updater.show_time = show_time

    if movie_id:
        updater.movie_id = movie_id

    if cinema_hall_id:
        cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
        updater.cinema_hall = cinema_hall

    updater.save()

    return updater


def delete_movie_session_by_id(session_id: int) -> None:

    movie_session = MovieSession.objects.get(id=session_id)
    movie_session.delete()
