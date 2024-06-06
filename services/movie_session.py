import datetime


from db.models import MovieSession, CinemaHall, Movie


def create_movie_session(
        movie_show_time: datetime.datetime,
        cinema_hall_id: int,
        movie_id: int
) -> None:
    cinema_hall_id = CinemaHall.objects.get(id=cinema_hall_id)
    movie = Movie.objects.get(id=movie_id)
    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=cinema_hall_id,
        movie=movie
    )


def get_movies_sessions(session_date: datetime.date = None) -> None:
    filters = {}
    if session_date:
        filters["show_time__date"] = session_date
    return MovieSession.objects.filter(**filters)


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int, show_time: datetime.datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> MovieSession:
    movie_session = get_movie_session_by_id(session_id)
    if show_time:
        movie_session.show_time = show_time
    if movie_id:
        movie_id = Movie.objects.get(id=movie_id)
        movie_session.movie_id = movie_id
    if cinema_hall_id:
        cinema_hall_id = CinemaHall.objects.get(id=cinema_hall_id)
        movie_session.cinema_hall_id = cinema_hall_id
    movie_session.save()
    return movie_session


def delete_movie_session_by_id(session_id: int) -> None:
    get_movie_session_by_id(session_id).delete()
