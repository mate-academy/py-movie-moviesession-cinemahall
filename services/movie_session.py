from db.models import MovieSession


def create_movie_session(movie_show_time, movie_id, cinema_hall_id):
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id,
    )


def get_movies_sessions(session_date=None):
    sessions = MovieSession.objects.all()
    if session_date is not None:
        sessions = sessions.filter(show_time__date=session_date)
    return sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id, show_time=None, movie_id=None, cinema_hall_id=None):
    session = MovieSession.objects.get(id=session_id)
    update_fields = []
    if show_time is not None:
        session.show_time = show_time
        update_fields.append("show_time")
    if movie_id is not None:
        session.movie_id = movie_id
        update_fields.append("movie")
    if cinema_hall_id is not None:
        session.cinema_hall_id = cinema_hall_id
        update_fields.append("cinema_hall")
    if update_fields:
        session.save(update_fields=update_fields)
    return session


def delete_movie_session_by_id(session_id):
    MovieSession.objects.get(id=session_id).delete()
