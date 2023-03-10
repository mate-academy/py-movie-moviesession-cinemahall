from db.models import MovieSession


def create_movie_session(movie_show_time,
                         movie_id,
                         cinema_hall_id):
    MovieSession.objects.create(show_time=movie_show_time,
                                cinema_hall_id=cinema_hall_id,
                                movie_id=movie_id)


def get_movies_sessions(session_date=None):
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    else:
        return MovieSession.objects.all()


def update_movie_session(session_id=None,
                         show_time=None,
                         movie_id=None,
                         cinema_hall_id=None):
    if show_time:
        MovieSession.objects.update(show_time=show_time)
    if movie_id:
        MovieSession.objects.update(movie_id=movie_id)
    if cinema_hall_id:
        MovieSession.objects.update(cinema_hall_id=cinema_hall_id)


def get_movie_session_by_id(movie_session_id):
    if movie_session_id:
        return MovieSession.objects.get(id=movie_session_id)


def delete_movie_session_by_id(session_id=None):
    if session_id:
        MovieSession.objects.filter(id=session_id).delete()
