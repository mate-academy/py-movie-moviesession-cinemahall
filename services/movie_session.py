from django.db.models import QuerySet

from db.models import Movie, CinemaHall, MovieSession


def create_movie_session(movie_show_time: str,
                         movie_id: int,
                         cinema_hall_id: int) -> MovieSession:
    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)

    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=cinema_hall,
        movie=movie
    )


def get_movies_sessions(session_date: str = None) -> QuerySet[MovieSession]:
    query = MovieSession.objects.all()
    if session_date:
        query = query.filter(show_time__date=session_date)

    return query


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: str = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> MovieSession:
    obj = MovieSession.objects.get(id=session_id)
    if show_time:
        obj.show_time = show_time
    if movie_id:
        obj.movie_id = movie_id
    if cinema_hall_id:
        obj.cinema_hall_id = cinema_hall_id

    obj.save()
    return obj


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
