from db.models import MovieSession


def create_movie_session(
        movie_show_time,
        movie_id: int,
        cinema_hall_id: int
):
    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id,
    )


def get_movies_sessions(session_date=None):
    queryset = MovieSession.objects.all()

    if session_date is not None:
        queryset = queryset.filter(show_time__date=session_date)

    return queryset


def get_movie_session_by_id(movie_session_id: int):
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        movie_id: int = None,
        show_time=None,
        cinema_hall_id: int = None
):
    movie_session = MovieSession.objects.filter(id=session_id)

    if movie_id:
        movie_session.update(movie_id=movie_id)

    if show_time:
        movie_session.update(show_time=show_time)

    if cinema_hall_id:
        movie_session.update(cinema_hall_id=cinema_hall_id)


def delete_movie_session_by_id(session_id: int):
    MovieSession.objects.filter(id=session_id).delete()
