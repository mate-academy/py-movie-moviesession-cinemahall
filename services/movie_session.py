from db.models import Movie, MovieSession, CinemaHall
import datetime


def create_movie_session(
        movie_show_time: int, movie_id: int, cinema_hall_id: int
) -> MovieSession:
    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie=movie,
        cinema_hall=cinema_hall
    )


def get_movies_sessions(session_date: int = None) -> MovieSession:
    if session_date:
        target_date = datetime.datetime.strptime(
            session_date, "%Y-%m-%d").date()

        movie_sessions = MovieSession.objects.filter(
            show_time__date=target_date
        )
    else:
        movie_sessions = MovieSession.objects.all()

    return movie_sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    movie_session = MovieSession.objects.get(id=movie_session_id)
    return movie_session


def update_movie_session(
        session_id: MovieSession,
        show_time: int = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> MovieSession:
    session = MovieSession.objects.get(id=session_id)

    if show_time is not None:
        session.show_time = show_time
    if movie_id is not None:
        session.movie_id = movie_id
    if cinema_hall_id is not None:
        session.cinema_hall_id = cinema_hall_id

    session.save()


def delete_movie_session_by_id(movie_session_id: int) -> MovieSession:
    movie_session = get_movie_session_by_id(movie_session_id)
    movie_session.delete()
