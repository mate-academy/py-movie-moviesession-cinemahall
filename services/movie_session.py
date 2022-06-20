from db.models import MovieSession, CinemaHall, Movie


def create_movie_session(
    movie_show_time,
    movie_id,
    cinema_hall_id
):
    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movies_sessions(session_date=None):
    queryset = MovieSession.objects.all()

    if session_date:
        return queryset.filter(show_time__date=session_date)

    return queryset


def get_movie_session_by_id(movie_session_id: int):
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time=None,
        movie_id: int = None,
        cinema_hall_id: int = None
):
    session = MovieSession.objects.filter(id=session_id)

    if show_time:
        session.update(show_time=show_time)

    if movie_id:
        session.update(movie_id=movie_id)

    if cinema_hall_id:
        session.update(cinema_hall_id=cinema_hall_id)


def delete_movie_session_by_id(session_id: int):
    MovieSession.objects.get(id=session_id).delete()
