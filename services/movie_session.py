import init_django_orm  # noqa: F401

from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(movie_show_time: str,
                         movie_id: int,
                         cinema_hall_id: int) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        movie=Movie.objects.get(id=movie_id),
        cinema_hall=CinemaHall.objects.get(id=cinema_hall_id))


def get_movies_sessions(session_date: str = None) -> MovieSession:
    session = MovieSession.objects.all()
    if session_date:
        return session.filter(show_time__date=session_date)
    return session


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: str = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> None:
    update = MovieSession.objects.get(id=session_id)
    if show_time:
        update.show_time = show_time
    if movie_id:
        update.movie_id = movie_id
    if cinema_hall_id:
        update.cinema_hall_id = cinema_hall_id
    update.save()


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()


if __name__ == "__main__":
    print(update_movie_session(session_id=1, cinema_hall_id=4))
