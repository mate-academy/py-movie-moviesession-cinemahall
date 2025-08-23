from db.models import MovieSession, Movie, CinemaHall
from django.core.exceptions import ObjectDoesNotExist


def create_movie_session(movie_show_time, movie_id, cinema_hall_id):
    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)

    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie=movie,
        cinema_hall=cinema_hall
    )


def get_movie_session(session_date=None):
    qs = MovieSession.objects.all()
    if session_date is None:
        qs = qs.filter(show_time__date=session_date)
    return qs


def get_movie_sessions_by_id(movie_session_id):
    return MovieSession.objects.filter(id=movie_session_id)


def update_movie_session(session_id, show_time=None, movie_id=None, cinema_hall_id=None):
    session = MovieSession.objects.get(id=session_id)
    if show_time:
        session.show_time = show_time
    if movie_id:
        session.movie_id = movie_id
    if cinema_hall_id:
        session.cinema_hall = cinema_hall_id
    session.save()
    return session


def delete_movie_session(session_id):

    try:
        session = MovieSession.objects.get(id=session_id)
        session.delete()
        return True
    except ObjectDoesNotExist:
        return False
