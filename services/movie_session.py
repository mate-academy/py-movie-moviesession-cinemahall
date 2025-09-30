from datetime import datetime, date

from django.db.models import QuerySet

from db.models import MovieSession, CinemaHall, Movie


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movies_sessions(session_date: str = None) -> QuerySet[MovieSession]:
    movie_sessions = MovieSession.objects.all()
    if session_date:
        year, month, day = session_date.split("-")
        movie_sessions = movie_sessions.filter(
            show_time__date=date(
                year=int(year),
                month=int(month),
                day=int(day)
            )
        )
    return movie_sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession | None:
    try:
        return MovieSession.objects.get(id=movie_session_id)
    except MovieSession.DoesNotExist:
        print(f"Movie session by id: {movie_session_id} does not exist!")
        return None


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> MovieSession | None:
    movie_session = get_movie_session_by_id(movie_session_id=session_id)
    if movie_session is not None:
        if show_time:
            movie_session.show_time = show_time
        if movie_id:
            if Movie.objects.filter(id=movie_id).exists():
                movie_session.movie_id = movie_id
        if cinema_hall_id:
            if CinemaHall.objects.filter(id=cinema_hall_id).exists():
                movie_session.cinema_hall_id = cinema_hall_id

    duplicat_movie_session = MovieSession.objects.filter(
        show_time=movie_session.show_time,
        cinema_hall_id=movie_session.cinema_hall_id
    )
    if (
            duplicat_movie_session
            and (cinema_hall_id or show_time)
            and not movie_id
    ):
        print(
            f"Cinema hall by date: {movie_session.show_time} "
            f"and hall id: {movie_session.cinema_hall_id} is busy!"
        )
        return None
    else:
        movie_session.save()
    return movie_session


def delete_movie_session_by_id(
        movie_session_id: int
) -> tuple[int, dict[str, int]] | None:
    movie_session = get_movie_session_by_id(movie_session_id)
    if movie_session:
        movie_session = movie_session.delete()
    return movie_session
