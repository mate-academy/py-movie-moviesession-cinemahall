from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> object:
    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie=movie,
        cinema_hall=cinema_hall
    )


def get_movies_sessions(session_date: str = None) -> object:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> object:
    try:
        return MovieSession.objects.get(id=movie_session_id)
    except MovieSession.DoesNotExist:
        return None


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> object | None:
    try:
        movie_session = get_movie_session_by_id(session_id)
        if show_time:
            movie_session.show_time = show_time
        if movie_id:
            movie_session.movie = Movie.objects.get(id=movie_id)
        if cinema_hall_id:
            movie_session.cinema_hall = CinemaHall.objects.get(
                id=cinema_hall_id
            )
        movie_session.save()
        return movie_session
    except MovieSession.DoesNotExist:
        return None


def delete_movie_session_by_id(session_id) -> None:
    get_movie_session_by_id(session_id).delete()
