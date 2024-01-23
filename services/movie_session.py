from db.models import MovieSession, CinemaHall, Movie


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> str:
    show_time = movie_show_time
    cinema_hall = CinemaHall.objects.get(pk=cinema_hall_id)
    movie = Movie.objects.get(pk=movie_id)
    movie_session = MovieSession.objects.create(
        show_time=show_time,
        cinema_hall=cinema_hall,
        movie=movie
    )
    return movie_session


def get_movies_sessions(session_date: str = None) -> str:
    sessions = MovieSession.objects.all()

    if session_date:
        sessions = sessions.filter(show_time__date=session_date)

    return sessions


def get_movie_session_by_id(session_id: int) -> str:
    return MovieSession.objects.get(id=session_id)


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None) -> None:
    session = MovieSession.objects.get(id=session_id)

    if show_time:
        session.show_time = show_time

    if movie_id:
        session.movie_id = movie_id

    if cinema_hall_id:
        session.cinema_hall_id = cinema_hall_id

    session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
