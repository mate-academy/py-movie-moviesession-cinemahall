from db.models import MovieSession
from db.models import Movie, CinemaHall


def update_movie_session(session_id, show_time=None, movie_id=None, cinema_hall_id=None):
    movie_session = MovieSession.objects.get(id=session_id)
    if show_time is not None:
        movie_session.show_time = show_time
    if movie_id is not None:
        movie_session.movie = Movie.objects.get(id=movie_id)
    if cinema_hall_id is not None:
        movie_session.cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    movie_session.save()
    return movie_session
