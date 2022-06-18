from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(movie_show_time,
                         movie_id: int,
                         cinema_hall_id: int):

    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    MovieSession.objects.create(show_time=movie_show_time,
                                cinema_hall=cinema_hall,
                                movie=movie)


def get_movies_sessions(session_date: str = None):

    movies = MovieSession.objects.all()
    if session_date:
        movies = MovieSession.objects.filter(show_time__date=session_date)

    return movies


def get_movie_session_by_id(movie_session_id: int):
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time=None,
                         movie_id=None,
                         cinema_hall_id=None):

    session_for_update = MovieSession.objects.filter(id=session_id)

    if show_time:
        session_for_update.update(show_time=show_time)

    if cinema_hall_id:
        new_cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
        session_for_update.update(cinema_hall=new_cinema_hall)

    if movie_id:
        new_movie = Movie.objects.get(id=movie_id)
        session_for_update.update(movie=new_movie)


def delete_movie_session_by_id(session_id: int):
    MovieSession.objects.filter(id=session_id).delete()
