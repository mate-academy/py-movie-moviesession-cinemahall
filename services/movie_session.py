from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int,
) -> QuerySet:
    movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )
    return movie_session


def get_movies_sessions(session_date: str = "") -> QuerySet:
    queryset = MovieSession.objects.all()
    if session_date:
        year, month, day = session_date.split("-")
        queryset = queryset.filter(
            show_time__year=year,
            show_time__month=month,
            show_time__day=day
        )
        return queryset
    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    if MovieSession.objects.filter(id=movie_session_id).exists():
        return MovieSession.objects.get(id=movie_session_id)
    return MovieSession.objects.filter(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None,

) -> MovieSession:
    session = get_movie_session_by_id(session_id)
    if show_time:
        session.show_time = show_time
    if movie_id:
        session.movie_id = movie_id
    if cinema_hall_id:
        session.cinema_hall_id = cinema_hall_id
    session.save()
    return session


def delete_movie_session_by_id(session_id: int) -> None:
    get_movie_session_by_id(session_id).delete()
