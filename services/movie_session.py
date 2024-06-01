from db.models import MovieSession


def create_movie_session(
        movie_show_time,
        movie_id,
        cinema_hall_id
):
    return MovieSession.objects.create(
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id,
        show_time=movie_show_time
    )


def get_movies_sessions(session_date=None):
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id):
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
    session_id,
    show_time=None,
    movie_id=None,
    cinema_hall_id=None
):
    movie_session = get_movie_session_by_id(session_id)
    if movie_session:
        if show_time:
            movie_session.show_time = show_time
        if movie_id:
            movie_session.movie_id = movie_id
        if cinema_hall_id:
            movie_session.cinema_hall_id = cinema_hall_id
        movie_session.save()
    return movie_session


def delete_movie_session_by_id(session_id):
    get_movie_session_by_id(session_id).delete()
