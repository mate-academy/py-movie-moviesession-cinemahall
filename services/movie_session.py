from django.db.models import QuerySet

from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(movie_show_time: str,
                         movie_id: int, cinema_hall_id: int) -> None:
    movie_ = Movie.objects.get(id=movie_id)
    cinema_hall_ = CinemaHall.objects.get(id=cinema_hall_id)
    MovieSession.objects.create(show_time=movie_show_time,
                                movie=movie_, cinema_hall=cinema_hall_)


def get_movies_sessions(session_date: str = None) -> QuerySet:
    movie_session = MovieSession.objects.all()
    if session_date:
        movie_session = movie_session.filter(show_time__date=session_date)
    return movie_session


def update_movie_session(session_id: int, show_time: str = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> None:
    try:
        movie_session = MovieSession.objects.get(id=session_id)
    except MovieSession.DoesNotExist:
        return

    if show_time is not None:
        movie_session.show_time = show_time
    if movie_id is not None:
        movie_session.movie_id = movie_id
    if cinema_hall_id is not None:
        movie_session.cinema_hall_id = cinema_hall_id

    movie_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    movie_session = MovieSession.objects.get(id=session_id)
    movie_session.delete()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    movie_session = MovieSession.objects.get(id=movie_session_id)
    return movie_session
