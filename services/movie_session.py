from db.models import MovieSession


def create_movie_session(movie_show_time, movie_id: int, cinema_hall_id: int):
    movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=cinema_hall_id,
        movie=movie_id
    )


def get_movies_sessions(session_date: str = None):
    queryset = MovieSession.objects.all()
    if session_date is not None:
        queryset = queryset.filter(show_time=session_date)
    return queryset


def get_movie_session_by_id(movie_session_id: int):
    return MovieSession.objects.filter(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None
):
    session = MovieSession.objects.get(id=session_id)
    if show_time is not None:
        session.show_time = show_time
    if movie_id is not None:
        session.movie = movie_id
    if cinema_hall_id is not None:
        session.cinema_hall_id = cinema_hall_id
    session.save()
