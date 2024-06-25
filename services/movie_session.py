from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinematically_id: int
) -> QuerySet:
    return MovieSession.objects.create(
        movie_id=movie_id,
        cinemahall_id=cinematically_id,
        show_time=movie_show_time
    )


def get_movies_sessions(movie_show_time: str | None) -> QuerySet:
    if movie_show_time:
        return MovieSession.objects.filter(
            show_time__date=movie_show_time
        )
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: id) -> QuerySet:
    return MovieSession.objects.filter(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: str | None = None,
        movie_id: int | None = None,
        cinema_hall_id: int | None = None
) -> QuerySet:

    movie = get_movie_session_by_id(session_id)
    if show_time:
        movie.show_time = show_time
    if movie_id:
        movie.movie_id = movie_id
    if cinema_hall_id:
        movie.cinematically_id = cinema_hall_id

    movie.save()
    return movie


def delete_movie_session_by_id(session_id: int) -> MovieSession:
    return get_movie_session_by_id(session_id).delete()