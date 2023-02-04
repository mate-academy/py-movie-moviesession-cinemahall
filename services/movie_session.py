from db.models import MovieSession, CinemaHall, Movie
from datetime import datetime as dt


def create_movie_session(
        movie_show_time: dt,
        movie_id: int,
        cinema_hall_id: int
) -> None:

    hall = CinemaHall.objects.get(id=cinema_hall_id)
    movie = Movie.objects.get(id=movie_id)
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=hall,
        movie=movie
    )


def get_movies_sessions(session_date: str = None) -> list[MovieSession]:
    date = dt.strptime(session_date, "%Y-%m-%d") if session_date else None
    if date:
        return MovieSession.objects.filter(show_time__date=date).all()
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:

    if MovieSession.objects.filter(id=session_id).exists():
        if show_time:
            MovieSession.objects.filter(id=session_id).update(
                show_time=show_time
            )
        if movie_id:
            movie_id = Movie.objects.get(id=movie_id)
            MovieSession.objects.filter(id=session_id).update(
                movie=movie_id
            )

        if cinema_hall_id:
            cinema_hall_id = CinemaHall.objects.get(id=cinema_hall_id)
            MovieSession.objects.filter(id=session_id).update(
                cinema_hall=cinema_hall_id
            )


def delete_movie_session_by_id(session_id: int) -> None:
    all_sessions = MovieSession.objects.all()
    if all_sessions.filter(id=session_id).exists():
        all_sessions.get(id=session_id).delete()
