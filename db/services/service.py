from db.models import Movie, Actor, Genre
from db.models import CinemaHall
from db.models import MovieSession
from django.utils import timezone

def get_movies(genres_ids=None, actors_ids=None):
    movies = Movie.objects.all()

    if genres_ids:
        movies = movies.filter(genres__id__in=genres_ids)
    if actors_ids:
        movies = movies.filter(actors__id__in=actors_ids)

    return movies.distinct()

def get_movie_by_id(movie_id):
    return Movie.objects.get(id=movie_id)

def create_movie(movie_title, movie_description, genres_ids=None, actors_ids=None):
    movie = Movie.objects.create(title=movie_title, description=movie_description)

    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)

    return movie

def get_cinema_halls():
    return CinemaHall.objects.all()

def create_cinema_hall(hall_name, hall_rows, hall_seats_in_row):
    return CinemaHall.objects.create(name=hall_name, rows=hall_rows, seats_in_row=hall_seats_in_row)

def create_movie_session(movie_show_time, movie_id, cinema_hall_id):
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )

def get_movies_sessions(session_date=None):
    sessions = MovieSession.objects.all()

    if session_date:
        sessions = sessions.filter(show_time__date=session_date)

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
    session = MovieSession.objects.get(id=session_id)
    session.delete()
