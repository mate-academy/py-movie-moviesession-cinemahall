import datetime

from db.models import MovieSession


def create_movie_session(movie_show_time,
                         movie_id: int,
                         cinema_hall_id: int):
    MovieSession.objects.create(
        show_time=movie_show_time,
        movie=movie_id,
        cinema_hall=cinema_hall_id,
    )


def get_movies_sessions(session_date):
    if session_date:
        return MovieSession.objects.all().filter(show_time=session_date)
    else:
        return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id):
    return MovieSession.objects.all().filter(id=movie_session_id)


def update_movie_session(session_id,
                         show_time=None,
                         movie_id=None,
                         cinema_hall_id=None):
    movie_session = MovieSession.objects.filter(id=session_id).update()
    if show_time:
        movie_session.show_time.set(show_time)
    if cinema_hall_id:
        movie_session.cinema_hall.set(cinema_hall_id)
    if movie_id:
        movie_session.movie.set(movie_id)


def delete_movie_session_by_id(session_id):
    MovieSession.objects.filter(id=session_id).delete()
