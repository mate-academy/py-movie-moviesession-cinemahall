from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(movie_show_time: str, movie_id: int,
                         cinema_hall_id: int) -> MovieSession:
    movie_session = MovieSession.objects.create(
        movie_show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id,
    )
    return movie_session


def get_movie_session(session_date: str) -> QuerySet:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    else:
        return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    movie_session = MovieSession.objects.get(id=movie_session_id)
    return movie_session


def update_movie_session(session_id: int, show_time: None,
                         movie_id: None,
                         cinema_hall_id: None) -> int:
    update_fields = {}
    if show_time:
        update_fields["show_time"] = show_time
    if movie_id:
        update_fields["movie_id"] = movie_id
    if cinema_hall_id:
        update_fields["cinema_hall_id"] = cinema_hall_id

    return MovieSession.objects.filter(id=session_id).update(**update_fields)


def delete_movie_session(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
