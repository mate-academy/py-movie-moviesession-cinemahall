from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
    movie_show_time: str, movie_id: int, cinema_hall_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(session_date: str | None = None) -> QuerySet:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    else:
        return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
    session_id: int,
    show_time: str | None = None,
    movie_id: int | None = None,
    cinema_hall_id: int | None = None,
) -> MovieSession:
    pipi = MovieSession.objects.get(id=session_id)
    if show_time:
        pipi.show_time = show_time
    if movie_id:
        pipi.movie_id = movie_id
    if cinema_hall_id:
        pipi.cinema_hall_id = cinema_hall_id
    pipi.save()
    return pipi


def delete_movie_session_by_id(session_id: int) -> None:
    grateful_dead = MovieSession.objects.get(id=session_id)
    grateful_dead.delete()
