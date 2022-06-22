from db.models import MovieSession


def create_movie_session(movie_show_time, movie_id, cinema_hall_id):
    MovieSession.objects.create(show_time=movie_show_time,
                                movie_id=movie_id,
                                cinema_hall_id=cinema_hall_id)


def get_movies_sessions(session_date=None):
    sessions = MovieSession.objects.all()
    if session_date:
        sessions.filter(show_time=session_date)
    return sessions


def get_movie_session_by_id(movie_session_id):
    movie = MovieSession.objects.get(id=movie_session_id).all()
    return movie


def update_movie_session(session_id, show_time=None,
                         movie_id=None, cinema_hall_id=None):
    session = MovieSession.objects.filter(id=session_id)
    if show_time:
        session.update(show_time=show_time)

    if movie_id:
        session.update(movie_id=movie_id)

    if cinema_hall_id:
        session.update(cinema_hall_id=cinema_hall_id)


def delete_movie_session_by_id(session_id):
    MovieSession.objects.filter(id=session_id).delete()
