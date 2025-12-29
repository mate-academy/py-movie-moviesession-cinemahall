from db.models import Movie
from db.models import CinemaHall
from db.models import MovieSession


def create_movie_session(movie_show_time: int,
                         movie_id: int,
                         cinema_hall_id: int
                         ) -> None:
    get_cinema_hall_id = CinemaHall.objects.get(
        id=cinema_hall_id
    )
    get_movie_id = Movie.objects.get(
        id=movie_id
    )

    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie=get_movie_id,
        cinema_hall=get_cinema_hall_id
    )


def get_movies_sessions(session_date: int = None) -> None:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> int:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: int = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None
                         ) -> None:
    update_session = MovieSession.objects.get(id=session_id)

    if show_time:
        update_session.show_time = show_time
        update_session.save()

    if movie_id:
        update_session.movie_id = movie_id
        update_session.save()

    if cinema_hall_id:
        update_session.cinema_hall_id = cinema_hall_id
        update_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    return MovieSession.objects.filter(id=session_id).delete()
