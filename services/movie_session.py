from db.models import MovieSession, Movie, CinemaHall
from django.db.models import QuerySet


def create_movie_session(
    movie_show_time: str, movie_id: int, cinema_hall_id: int
) -> MovieSession:
    """
    Create a movie session with the provided parameters.
    """
    try:
        movie = Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        raise ValueError(f"Movie with id {movie_id} does not exist.")
    try:
        cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    except CinemaHall.DoesNotExist:
        raise ValueError(
            f"CinemaHall with id {cinema_hall_id} does not exist."
        )
    return MovieSession.objects.create(
        show_time=movie_show_time, movie=movie, cinema_hall=cinema_hall
    )


def get_movies_sessions(session_date: str = None) -> QuerySet:
    """
    Retrieve movie sessions filtered by date if provided.
    """
    queryset = MovieSession.objects.all()

    if session_date:
        queryset = queryset.filter(
            show_time__date=session_date
        )  # Django обрабатывает строку "YYYY-MM-DD"

    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    """
    Retrieve a movie session by its ID.
    """
    try:
        return MovieSession.objects.get(id=movie_session_id)
    except MovieSession.DoesNotExist:
        raise ValueError(
            f"Movie session with id {movie_session_id} does not exist."
        )


def update_movie_session(
    session_id: int,
    show_time: str = None,
    movie_id: int = None,
    cinema_hall_id: int = None,
) -> MovieSession:
    """
    Update a movie session with the provided parameters.
    """
    try:
        movie_session = MovieSession.objects.get(id=session_id)
    except MovieSession.DoesNotExist:
        raise ValueError(
            f"Movie session with id {session_id} does not exist."
        )

    if show_time:
        movie_session.show_time = show_time
    if movie_id:
        movie_session.movie = Movie.objects.get(id=movie_id)
    if cinema_hall_id:
        movie_session.cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)

    movie_session.save()
    return movie_session


def delete_movie_session_by_id(session_id: int) -> None:
    """
    Delete a movie session by its ID.
    """
    movie_session = MovieSession.objects.get(id=session_id)
    movie_session.delete()
