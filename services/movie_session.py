from datetime import datetime, date

from django.db.models import QuerySet

from db.models import MovieSession, CinemaHall, Movie


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession | None:
    validate_cinema_hall_id = CinemaHall.objects.filter(id=cinema_hall_id)
    validate_movie_id = Movie.objects.filter(id=movie_id)

    if not validate_movie_id:
        print(f"The movie with id: {movie_id} does not exist!")
        return None
    if not validate_cinema_hall_id:
        print(f"The cinema hall with id: {cinema_hall_id} does not exist!")
        return None
    else:
        movie_session, create = MovieSession.objects.get_or_create(
            show_time=movie_show_time,
            cinema_hall_id=cinema_hall_id,
            defaults={
                "movie_id": movie_id
            }
        )
        if not create:
            print(
                f"The movie session for datetime: '{movie_show_time}' and "
                f"cinema hall with id: {cinema_hall_id} already exist!"
            )
        return movie_session


def get_movies_sessions(session_date: str = None) -> None | QuerySet:
    movie_sessions = MovieSession.objects.all()
    if session_date:
        try:
            datetime.strptime(session_date, "%Y-%m-%d")
            year, month, day = session_date.split("-")
            movie_sessions = movie_sessions.filter(
                show_time__date=date(
                    year=int(year),
                    month=int(month),
                    day=int(day)
                )
            )
        except ValueError:
            print(
                f"Invalid format '{session_date}', "
                f"please enter like '2025-10-11'"
            )
            return None
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
    if movie_session:
        if show_time:
            movie_session.show_time = show_time
        if movie_id:
            if Movie.objects.filter(id=movie_id).exists():
                movie_session.movie_id = movie_id
            else:
                print(f"Movie with id: {movie_id} does not exist!")
        if cinema_hall_id:
            if CinemaHall.objects.filter(id=cinema_hall_id).exists():
                movie_session.cinema_hall_id = cinema_hall_id
            else:
                print(f"Cinema hall with id: {cinema_hall_id} does not exist!")

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
