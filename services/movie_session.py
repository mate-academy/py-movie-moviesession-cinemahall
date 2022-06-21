from db.models import MovieSession


def create_movie_session(movie_show_time, movie_id: int, cinema_hall_id: int):
    new_movie = MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )
    return new_movie


def get_movies_sessions(session_date: str = None):
    if session_date is not None:
        year, month, day = session_date.split("-")
        return MovieSession.objects.filter(
            show_time__year=year,
            show_time__month=month,
            show_time__day=day
        )
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int):
    return MovieSession.objects.get(pk=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time=None,
        movie_id: int = None,
        cinema_hall_id: int = None
):
    session_to_update = MovieSession.objects.filter(pk=session_id)

    if show_time is not None:
        session_to_update.update(show_time=show_time)

    if movie_id is not None:
        session_to_update.update(movie_id=movie_id)

    if cinema_hall_id is not None:
        session_to_update.update(cinema_hall_id=cinema_hall_id)

    return session_to_update


def delete_movie_session_by_id(session_id):
    MovieSession.objects.get(pk=session_id).delete()
