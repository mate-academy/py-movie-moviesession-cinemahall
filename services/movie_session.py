from db.models import MovieSession


def create_movie_session(
        movie_show_time: int,
        movie_id: id,
        cinema_hall_id: int
) -> None:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(session_date: None = None) -> None:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: None) -> None:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: None,
        show_time: None = None,
        movie_id: None = None,
        cinema_hall_id: None = None
) -> None:
    movie_session = MovieSession.objects.get(id=session_id)
    if show_time:
        movie_session.show_time = show_time
    if movie_id:
        movie_session.movie_id = movie_id
    if cinema_hall_id:
        movie_session.cinema_hall_id = cinema_hall_id
    movie_session.save()
    return movie_session


def delete_movie_session_by_id(session_id: None) -> None:
    MovieSession.objects.filter(id=session_id).delete()
