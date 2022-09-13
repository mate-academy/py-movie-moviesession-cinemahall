from db.models import MovieSession


def create_movie_session(movie_show_time, movie_id, cinema_hall_id):
    MovieSession.objects.create(show_time=movie_show_time,
                                cinema_hall_id=cinema_hall_id,
                                movie_id=movie_id)


def get_movies_sessions(session_date=None):
    queryset = MovieSession.objects.all()
    if session_date:
        session_date = session_date.split("-")
        queryset = queryset.filter(show_time__year=session_date[0],
                                   show_time__month=session_date[1],
                                   show_time__day=session_date[2])
    return queryset


def get_movie_session_by_id(movie_session_id):
    return MovieSession.objects.get(pk=movie_session_id)


def update_movie_session(session_id,
                         show_time=None,
                         movie_id=None,
                         cinema_hall_id=None):
    queryset = MovieSession.objects.filter(pk=session_id)
    if show_time:
        queryset.update(show_time=show_time)
    if movie_id:
        queryset.update(movie_id=movie_id)
    if cinema_hall_id:
        queryset.update(cinema_hall_id=cinema_hall_id)


def delete_movie_session_by_id(session_id):
    MovieSession.objects.filter(pk=session_id).delete()
