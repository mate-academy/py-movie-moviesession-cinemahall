from datetime import datetime, date

from django.db.models import QuerySet

from db.models import MovieSession, CinemaHall, Movie


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    movie = Movie.objects.get(id=movie_id)
    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=cinema_hall,
        movie=movie
    )


def get_movies_sessions(session_date: date = None) -> QuerySet[MovieSession]:
    queryset = MovieSession.objects.all()
    if session_date:
        return queryset.filter(show_time__date=session_date)
    return queryset


def get_movie_session_by_id(id_: int) -> MovieSession:
    return MovieSession.objects.get(id=id_)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> MovieSession:
    movie_session_for_update = MovieSession.objects.get(id=session_id)
    if show_time:
        movie_session_for_update.show_time = show_time
    if movie_id:
        movie_session_for_update.movie_id = movie_id
    if cinema_hall_id:
        movie_session_for_update.cinema_hall_id = cinema_hall_id
    movie_session_for_update.save()
    return movie_session_for_update


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
