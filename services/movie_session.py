from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(
        session_date: str | None = None
) -> QuerySet[MovieSession]:
    queryset = MovieSession.objects.all()
    if session_date:
        queryset = queryset.filter(show_time__date=session_date)
    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(pk=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: str | None = None,
        movie_id: int | None = None,
        cinema_hall_id: int | None = None
) -> MovieSession:
    update_fields = {}

    if show_time:
        update_fields["show_time"] = show_time
    if movie_id:
        update_fields["movie_id"] = movie_id
    if cinema_hall_id:
        update_fields["cinema_hall_id"] = cinema_hall_id

    try:
        movie_session = MovieSession.objects.get(id=session_id)
        if update_fields:
            MovieSession.objects.filter(id=session_id).update(**update_fields)
            movie_session.refresh_from_db()
        return movie_session
    except MovieSession.DoesNotExist:
        raise ValueError(f"MovieSession with id {session_id} does not exist")


def delete_movie_session_by_id(movie_session_id: int) -> None:
    movie_session = get_movie_session_by_id(movie_session_id)
    movie_session.delete()
