from db.models import MovieSession


def create_movie_session(
        movie_show_time,
        movie_id: int,
        cinema_hall_id
):
    new_movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )

    return new_movie_session


def get_movies_sessions(session_date=None):
    if session_date is not None:
        return MovieSession.objects.filter(show_time__date=session_date)

    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int):
    return MovieSession.objects.filter(id=movie_session_id)[0]


def update_movie_session(
        session_id: int,
        show_time=None,
        movie_id=None,
        cinema_hall_id=None
):
    updated_movi_session = MovieSession.objects.filter(id=session_id)[0]
    if show_time is not None:
        updated_movi_session.show_time = show_time

    if movie_id is not None:
        updated_movi_session.movie_id = movie_id

    if cinema_hall_id is not None:
        updated_movi_session.cinema_hall_id = cinema_hall_id

    updated_movi_session.save()


def delete_movie_session_by_id(session_id: int):
    MovieSession.objects.filter(id=session_id).delete()
