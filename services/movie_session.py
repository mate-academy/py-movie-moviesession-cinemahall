from datetime import datetime

from django.db.models import QuerySet

from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    if cinema_hall_id:
        cinema_hall_id = CinemaHall.objects.get(id=cinema_hall_id)

    if movie_id:
        movie_id = Movie.objects.get(id=movie_id)

    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=cinema_hall_id,
        movie=movie_id,
    )


def get_movies_sessions(session_date: datetime = None) -> QuerySet:
    if session_date:
        return MovieSession.objects.filter(
            show_time__date=session_date
        )
    else:
        return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> MovieSession:
    update_fields = {}

    if show_time:
        update_fields["show_time"] = show_time

    if cinema_hall_id:
        cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
        update_fields["cinema_hall"] = cinema_hall

    if movie_id:
        movie = Movie.objects.get(id=movie_id)
        update_fields["movie"] = movie

    MovieSession.objects.filter(id=session_id).update(**update_fields)
    return MovieSession.objects.get(id=session_id)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
