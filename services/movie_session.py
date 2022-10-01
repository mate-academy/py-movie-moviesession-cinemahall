import datetime

from db.models import MovieSession, CinemaHall, Movie


def create_movie_session(movie_show_time, movie_id, cinema_hall_id):
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=CinemaHall.objects.get(id=cinema_hall_id),
        movie=Movie.objects.get(id=movie_id)
    )


def get_movies_sessions(session_date: str = None):
    session = MovieSession.objects.all()

    if session_date is not None:
        session = session.filter(
            show_time__date=datetime.date(
                int(session_date.split("-")[0]),
                int(session_date.split("-")[1]),
                int(session_date.split("-")[2]),
            )
        )

    return session


def get_movie_session_by_id(movie_session_id):
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time=None,
        movie_id: int = None,
        cinema_hall_id: int = None
):
    session = MovieSession.objects.filter(id=session_id)

    if show_time is not None:
        session.update(show_time=show_time)

    if movie_id is not None:
        session.update(movie=Movie.objects.get(id=movie_id))

    if cinema_hall_id is not None:
        session.update(cinema_hall=CinemaHall.objects.get(id=cinema_hall_id))


def delete_movie_session_by_id(session_id):
    MovieSession.objects.get(id=session_id).delete()
