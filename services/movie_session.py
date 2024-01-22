from db.models import MovieSession


def create_movie_session(movie_show_time, movie_id: int, cinema_hall_id: int) -> None:
    MovieSession.objects.create(show_time=movie_show_time,
                                movie_id=movie_id,
                                cinema_hall_id=cinema_hall_id)


def get_movies_sessions(session_date: str = None) -> list[MovieSession]:
    if session_date is not None:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> str:
    return MovieSession.objects.filter(id=movie_session_id).first()


def update_movie_session(session_id: int, show_time: int = None,
                         movie_id: int = None, cinema_hall_id: int = None) -> None:
    update_fields = {}
    if show_time is not None:
        update_fields["show_time"] = show_time
    if movie_id is not None:
        update_fields["movie"] = movie_id
    if cinema_hall_id is not None:
        update_fields["cinema_hall"] = cinema_hall_id
    if update_fields:
        MovieSession.objects.filter(id=session_id).update(**update_fields)


def delete_movie_session_by_id(session_id: int) -> None:
    result = MovieSession.objects.filter(id=session_id)
    result.delete()
