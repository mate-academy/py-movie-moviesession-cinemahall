from db.models import MovieSession
from django.db.models.query import QuerySet
from datetime import datetime

def create_movie_session(movie_show_time, movie_id, cinema_hall_id) -> None:
    new_obj = MovieSession.objects.create(show_time=movie_show_time, cinema_hall=cinema_hall_id, movie=movie_id)
    new_obj.save()
    return None

def get_movies_sessions(session_date: str) -> QuerySet:
    if session_date:
        return MovieSession.objects.all().filter(time=datetime.strptime)
    else:
        return MovieSession.objects.all()

def get_movie_session_by_id(movie_session_id: int):
    return MovieSession.objects.all().get(id=movie_session_id)

def update_movie_session(session_id, show_time, movie_id, cinema_hall_id):
    new_obj = MovieSession.objects.all().filter(id=session_id)
    new_obj.update(show_time=show_time, movie=movie_id, cinema_hall=cinema_hall_id)


def delete_movie_session(session_id: int):
    new_obj = MovieSession.objects.all().filter(id=session_id)
    new_obj.delete()
