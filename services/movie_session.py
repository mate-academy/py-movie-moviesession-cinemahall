from db.models import MovieSession, Movie, CinemaHall
from django.db.models import QuerySet


def create_movie_session(movie_show_time: str,
                         movie_id: int,
                         cinema_hall_id: int) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=CinemaHall.objects.get(id=cinema_hall_id),
        movie=Movie.objects.get(id=movie_id)
    )


def get_movies_sessions(session_date: str = None) -> QuerySet:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession | None:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: str = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None
                         ) -> MovieSession | None:
    filtered = MovieSession.objects.get(id=session_id)

    if show_time:
        filtered.show_time = show_time
    if movie_id:
        filtered.movie = Movie.objects.get(id=movie_id)
    if cinema_hall_id:
        filtered.cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    filtered.save()


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()