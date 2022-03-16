from db.models import MovieSession, CinemaHall, Movie


def create_movie_session(
        movie_show_time,
        movie_id: int,
        cinema_hall_id: int,
):

    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id,
    )


def get_movies_sessions(
        session_date=None,
):
    result = MovieSession.objects.all()

    if session_date:
        result = result.filter(
            show_time__date=session_date,
        )

    return result


def get_movie_session_by_id(
        movie_session_id: int,
):
    return MovieSession.objects.get(
        id=movie_session_id,
    )


def update_movie_session(
        session_id: int,
        show_time=None,
        movie_id=None,
        cinema_hall_id=None,
):
    to_update = MovieSession.objects.all().filter(
        id=session_id,
    )
    if show_time:
        to_update.update(
            show_time=show_time,
        )

    if movie_id:
        to_update.update(movie=movie_id)

    if cinema_hall_id:
        to_update.update(cinema_hall=cinema_hall_id)

    return to_update


def delete_movie_session_by_id(
        session_id: int,

):
    return MovieSession.objects.get(id=session_id).delete()
