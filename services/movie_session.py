from datetime import datetime
from db.models import MovieSession


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> None:
    return MovieSession.objects.create(movie_id=movie_id,
                                       cinema_hall_id=cinema_hall_id,
                                       show_time=movie_show_time)


def get_movie_session_by_id(movie_session_id: int) -> None:
    return MovieSession.objects.get(id=movie_session_id)


def delete_movie_session_by_id(session_id: int) -> None:
    return MovieSession.objects.filter(id=session_id).delete()


def update_movie_session(session_id: int,
                         show_time: datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> None:
    try:
        movie_session = MovieSession.objects.get(id=session_id)
        if show_time:
            movie_session.show_time = show_time
        if movie_id:
            movie_session.movie_id = movie_id
        if cinema_hall_id:
            movie_session.cinema_hall_id = cinema_hall_id
        movie_session.save()
    except MovieSession.DoesNotExist:
        raise ValueError("Сеанс фільму з таким id не знайдений.")


def get_movies_sessions(session_date: datetime = None) -> None:
    if session_date is not None:
        norm_date = datetime.strptime(session_date, "%Y-%m-%d")
        return MovieSession.objects.filter(show_time__date=norm_date)
    else:
        return MovieSession.objects.all()
