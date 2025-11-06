from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(movie_show_time, movie_id, cinema_hall_id):
    session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=cinema_hall_id,
        movie=movie_id,
    )

    return session


def get_movie_session(session_id):
    session = session_id
    return session

def update_movie_session(session_id, show_time=None, movie_id=None, cinema_hall_id=None):
    session = MovieSession.objects.get(id=session_id)

    if show_time is not None:
        session.show_time = show_time
    if movie_id is not None:
        session.movie = movie_id
    if cinema_hall_id is not None:
        session.cinema_hall = cinema_hall_id

    session.save()
    return session
