from typing_extensions import Any

from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(movie_show_time, movie_id, cinema_hall_id) -> MovieSession:

    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)

    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie=movie,
        cinema_hall=cinema_hall
    )

def get_movies_sessions(session_date=None) -> Any:
    if session_date:
        return MovieSession.objects.filter(
            show_time__date = session_date
        )
    return MovieSession.objects.all()

def get_movie_session_by_id(movie_session_id) -> MovieSession:
    return MovieSession.objects.get(pk=movie_session_id)

def update_movie_session(session_id, show_time=None, movie_id=None, cinema_hall_id=None) -> int:
    update = {}
    if show_time is not None:
        update['show_time'] = show_time
    if movie_id is not None:
        movie = Movie.objects.get(id=movie_id)
        update['movie'] = movie
    if cinema_hall_id is not None:
        cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
        update['cinema_hall'] = cinema_hall
    return MovieSession.objects.filter(id=session_id).update(**update)

def delete_movie_session_by_id(session_id):
    MovieSession.objects.get(pk=session_id).delete()