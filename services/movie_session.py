from db.models import MovieSession


def create_movie_session(
        movie_show_time,
        movie_id: int,
        cinema_hall_id: int
):
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(session_date: str = None):
    queryset = MovieSession.objects.all()

    if session_date is not None:
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
    session_for_update = MovieSession.objects.filter(id=session_id)

    if show_time is not None:
        session_for_update.update(show_time=show_time)

    if movie_id is not None:
        session_for_update.update(movie=movie_id)

    if cinema_hall_id is not None:
        session_for_update.update(cinema_hall=cinema_hall_id)

    return session_for_update


def delete_movie_session_by_id(session_id: int):
    return MovieSession.objects.filter(id=session_id).delete()
