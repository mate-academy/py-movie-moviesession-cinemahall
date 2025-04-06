from db.models import MovieSession, Movie, CinemaHall
from datetime import datetime


def create_movie_session(movie_show_time: datetime, movie_id: int, cinema_hall_id: int):
    if movie_show_time and movie_id and cinema_hall_id:
        return MovieSession.objects.create(show_time=movie_show_time, movie_id=movie_id, cinema_hall_id=cinema_hall_id)


def get_movies_sessions(session_date: str = None):
    if session_date:
        date_obj = datetime.strptime(session_date, "%Y-%m-%d").date()
        return MovieSession.objects.filter(show_time__date=date_obj)

    return MovieSession.objects.all()


def update_movie_session(session_id: int, show_time: str = None, movie_id: int = None, cinema_hall_id: int = None):
    movie_session = MovieSession.objects.get(id=session_id)
    if show_time:
        movie_session.show_time = show_time

    if movie_id:
        movie_session.movie = Movie.objects.get(id=movie_id)

    if cinema_hall_id:
        movie_session.cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)

    movie_session.save()

def delete_movie_session_by_id(session_id: int):
    movie_session = MovieSession.objects.get(id=session_id)
    if movie_session:
        movie_session.delete()
    else:
        pass