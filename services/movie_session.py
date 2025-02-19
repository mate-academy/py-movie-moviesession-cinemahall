from db.models import MovieSession
from django.utils.dateparse import parse_date

def create_movie_session(movie_show_time, movie_id, cinema_hall_id):
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )

def get_movies_sessions(session_date=None):
    sessions = MovieSession.objects.all()
    if session_date:
        date_obj = parse_date(session_date)
        sessions = sessions.filter(show_time__date=date_obj)
    return sessions

def get_movie_session_by_id(movie_session_id):
    return MovieSession.objects.get(id=movie_session_id)

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
    MovieSession.objects.filter(id=session_id).delete()
