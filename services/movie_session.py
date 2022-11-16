from django.db.models import QuerySet

from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(movie_show_time: int,
                         movie_id: int,
                         cinema_hall_id: int) -> Movie:
    new_movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie=Movie.objects.get(id=movie_id),
        cinema_hall=CinemaHall.objects.get(id=cinema_hall_id)
    )
    return new_movie_session


def get_movies_sessions(session_date: str = None) -> QuerySet:
    queryset = MovieSession.objects.all()

    if session_date is not None:
        queryset = queryset.filter(show_time__date=session_date)

    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         movie_id: int = None,
                         show_time: str = None,
                         cinema_hall_id: int = None) -> QuerySet:

    queryset = MovieSession.objects.filter(id=session_id)

    if movie_id:
        queryset.update(movie_id=movie_id)

    if show_time:
        queryset.update(show_time=show_time)

    if cinema_hall_id:
        queryset.update(cinema_hall_id=cinema_hall_id)

    return queryset


def delete_movie_session_by_id(session_id: int) -> QuerySet:
    return MovieSession.objects.filter(id=session_id).delete()
