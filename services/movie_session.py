from db.models import MovieSession


def create_movie_session(
        movie_show_time: str,
        cinema_hall_id: int,
        movie_id: int
):
    new_movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id,
    )

    return new_movie_session


def get_movies_sessions(session_date: str = None):
    queryset = MovieSession.objects.all()

    if session_date:
        queryset = queryset.filter(show_time__date=session_date)

    return queryset


def get_movie_session_by_id(movie_session_id: int):
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None
):
    updating_session = MovieSession.objects.filter(id=session_id)

    if show_time:
        updating_session.update(show_time=show_time)

    if movie_id:
        updating_session.update(movie_id=movie_id)

    if cinema_hall_id:
        updating_session.update(cinema_hall_id=cinema_hall_id)

    return updating_session


def delete_movie_session_by_id(session_id):
    MovieSession.objects.filter(id=session_id).delete()
