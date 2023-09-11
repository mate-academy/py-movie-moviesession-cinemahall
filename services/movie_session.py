from datetime import datetime
from db.models import MovieSession, CinemaHall, Movie


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    try:
        movie = Movie.objects.get(pk=movie_id)
        cinema_hall = CinemaHall.objects.get(pk=cinema_hall_id)
        movie_session = MovieSession.objects.create(
            show_time=movie_show_time,
            movie=movie,
            cinema_hall=cinema_hall
        )
        return movie_session
    except (Movie.DoesNotExist, CinemaHall.DoesNotExist):
        return None


def get_movies_sessions(session_date: str = None) -> None:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    else:
        return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    try:
        movie_session = MovieSession.objects.get(pk=movie_session_id)
        return movie_session
    except MovieSession.DoesNotExist:
        return None


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    try:
        movie_session = MovieSession.objects.get(pk=session_id)

        if show_time:
            movie_session.show_time = show_time
        if movie_id:
            movie = Movie.objects.get(pk=movie_id)
            movie_session.movie = movie
        if cinema_hall_id:
            cinema_hall = CinemaHall.objects.get(pk=cinema_hall_id)
            movie_session.cinema_hall = cinema_hall

        movie_session.save()
    except MovieSession.DoesNotExist:
        pass


def delete_movie_session_by_id(session_id: int) -> None:
    try:
        movie_session = MovieSession.objects.get(pk=session_id)
        movie_session.delete()
    except MovieSession.DoesNotExist:
        pass
