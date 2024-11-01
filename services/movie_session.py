from django.db.models import QuerySet

from db.models import MovieSession, CinemaHall, Movie


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: str
) -> MovieSession:
    if cinema_hall_id:
        try:
            cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
        except CinemaHall.DoesNotExist:
            raise ValueError(f"CinemaHall with id={cinema_hall_id} does not exist.")
    if movie_id:
        try:
            movie = Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            raise ValueError(f"CinemaHall with id={movie_id} does not exist.")

    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=cinema_hall,
        movie=movie
    )


def get_movies_sessions(session_date: str = None) -> QuerySet[MovieSession]:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(
        movie_session_id: str = None
) -> MovieSession:
    if movie_session_id:
        try:
            return MovieSession.objects.get(id=movie_session_id)
        except MovieSession.DoesNotExist:
            raise ValueError(f"MovieSession with id={movie_session_id} does not exist.")
    return MovieSession.objects.all()


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    movie_session_update = MovieSession.objects.filter(id=session_id)
    if show_time:
        movie_session_update.update(show_time=show_time)
    if movie_id:
        movie_session_update.update(movie_id=movie_id)
    if cinema_hall_id:
        movie_session_update.update(cinema_hall_id=cinema_hall_id)


def delete_movie_session_by_id(session_id: int) -> None:
    session_delete = MovieSession.objects.get(id=session_id)
    session_delete.delete()
