from db.models import MovieSession, CinemaHall


def create_movie_session(movie_show_time: int,
                         movie_id: int,
                         cinema_hall_id: int) -> MovieSession:

    cinema_hall_instance = CinemaHall.objects.get(id=cinema_hall_id)

    new_movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=cinema_hall_instance,
        movie_id=movie_id
    )
    return new_movie_session


def get_movies_sessions(session_date: int = None) -> MovieSession:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: int = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> MovieSession:
    movie_session = MovieSession.objects.get(id=session_id)

    if show_time:
        movie_session.show_time = show_time
    if movie_id:
        movie_session.movie_id = movie_id
    if cinema_hall_id:
        movie_session.cinema_hall_id = cinema_hall_id

    movie_session.save()

    return movie_session


def delete_movie_session_by_id(session_id: int) -> MovieSession:
    return MovieSession.objects.filter(id=session_id).delete()
