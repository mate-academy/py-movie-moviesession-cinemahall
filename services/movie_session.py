from db.models import Movie, CinemaHall, MovieSession


def create_movie_session(
        movie_show_time: int,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:

    cinema_hall_id = CinemaHall.objects.get(id=cinema_hall_id)
    id_movie = Movie.objects.get(id=movie_id)

    movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=cinema_hall_id,
        movie=id_movie
    )

    return movie_session


def get_movies_sessions(session_date: str = None) -> MovieSession:

    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    else:
        return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:

    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: int = None,
        movie_id: int = None,
        cinema_hall_id: int = None) -> MovieSession:

    movie_to_update = MovieSession.objects.filter(id=session_id)
    if show_time:
        movie_to_update.update(show_time=show_time)
    if movie_id:
        movie_to_update.update(movie=movie_id)
    if cinema_hall_id:
        movie_to_update.update(cinema_hall=cinema_hall_id)


def delete_movie_session_by_id(session_id: int) -> MovieSession:
    return MovieSession.objects.filter(id=session_id).delete()
