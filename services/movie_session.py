from db.models import MovieSession


def create_movie_session(
        movie_show_time,
        movie_id: int,
        cinema_hall_id: int
):
    new_movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )

    return new_movie_session


def get_movies_sessions(session_date=None):
    movies_sessions = MovieSession.objects.all()

    if session_date:
        movies_sessions = movies_sessions.filter(show_time__date=session_date)

    return movies_sessions


def get_movie_session_by_id(movie_session_id: int):
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time=None,
        movie_id: int = None,
        cinema_hall_id: int = None
):
    update_session = MovieSession.objects.filter(id=session_id)

    if show_time:
        update_session.update(show_time=show_time)
    if movie_id:
        update_session.update(movie=movie_id)
    if cinema_hall_id:
        update_session.update(cinema_hall=cinema_hall_id)

    return update_session


def delete_movie_session_by_id(session_id: int):
    return MovieSession.objects.filter(id=session_id).delete()
