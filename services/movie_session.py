from db.models import MovieSession


def create_movie_session(movie_show_time: str,
                         movie_id: int,
                         cinema_hall_id: int
                         ) -> None:
    MovieSession.objects.create(show_time=movie_show_time,
                                movie_id=movie_id,
                                cinema_hall_id=cinema_hall_id)


def get_movies_sessions(session_date: str = None) -> object:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_sessions_id: int) -> object:

    return MovieSession.objects.get(id=movie_sessions_id)


def update_movie_session(session_id: int,
                         show_time: str = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None
                         ) -> None:
    update_data = {}
    if show_time:
        update_data["show_time"] = show_time
    if movie_id:
        update_data["movie_id"] = movie_id
    if cinema_hall_id:
        update_data["cinema_hall_id"] = cinema_hall_id
    MovieSession.objects.filter(id=session_id).update(**update_data)


def delete_movie_session_by_id(session_id: int) -> None:
    movie = MovieSession.objects.get(id=session_id)
    movie.delete()
