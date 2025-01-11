from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(movie_id: int,
                         cinema_hall_id: int,
                         cinema_id: int) -> None:
    MovieSession.objects.create(movie_id=movie_id,
                                cinema_hall_id=cinema_hall_id,
                                cinema_id=cinema_id)


def get_movies_sessions(session_date: int) -> QuerySet:
    if session_date:
        return MovieSession.objects.filter(session_date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(movie_session_id: int,
                         session_date: int,
                         cinema_hall_id: int,
                         cinema_id: int) -> None:
    movie_session = MovieSession.objects.get(id=movie_session_id)

    if session_date:
        movie_session.session_date = session_date
    if cinema_hall_id:
        movie_session.cinema_hall_id = cinema_hall_id
    if cinema_id:
        movie_session.cinema_id = cinema_id

    movie_session.save()


def delete_movie_session_by_id(movie_session_id: int) -> None:
    MovieSession.objects.get(id=movie_session_id).delete()
