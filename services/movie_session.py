from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int) -> None:
    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=cinema_hall,
        movie=movie
    )


def get_movies_sessions(session_date: str = None) -> list:
    if session_date is not None:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None) -> None:
    session = MovieSession.objects.get(id=session_id)

    if show_time is not None:
        session.show_time = show_time

    if movie_id is not None:
        movie = Movie.objects.get(id=movie_id)
        session.movie = movie

    if cinema_hall_id is not None:
        cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
        session.cinema_hall = cinema_hall

    session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    session = MovieSession.objects.get(id=session_id)
    session.delete()
