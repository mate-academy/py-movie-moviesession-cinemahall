from db.models import MovieSession
from datetime import datetime

def create_movie_session(movie_show_time, movie_id, cinema_hall_id):
     return MovieSession.objects.create(
        movie_id=movie_id,
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id
    )

def get_movies_sessions(session_date=None):
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    else:
        return MovieSession.objects.all()


def get_movie_session_by_id(movie_id):
    return MovieSession.objects.get(movie_id=movie_id)


def update_movie_session(session_id, show_time=None, movie_id=None, cinema_hall_id=None):
    session = MovieSession.objects.get(id=session_id)
    if show_time:
        session.show_time = show_time
    if movie_id:
        session.movie_id = movie_id
    if cinema_hall_id:
        session.cinema_hall_id = cinema_hall_id
    session.save()
    return session

def delete_movie_session_by_id(session_id):
    return MovieSession.objects.get(id=session_id).delete()
