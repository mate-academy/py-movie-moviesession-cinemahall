from django.db.models import QuerySet

from db.models import MovieSession, CinemaHall, Movie


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int) -> None:
    movie_session = MovieSession.objects.create(show_time=movie_show_time)
    create_hall = CinemaHall.objects.get(id=cinema_hall_id)
    create_movie = Movie.objects.get(id=movie_id)
    movie_session.cinema_hall = create_hall
    movie_session.movie = create_movie
    movie_session.save()


def get_movies_sessions(session_date: str = None) -> QuerySet:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    else:
        return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int, /,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> MovieSession:
    update_movie = MovieSession.objects.get(id=session_id)
    if show_time:
        update_movie = MovieSession.objects.get(show_time__date=show_time)

    if movie_id:
        update_movie = Movie.objects.get(id=movie_id)
        update_movie.movie = update_movie

    if cinema_hall_id:
        update_hall = CinemaHall.objects.get(id=cinema_hall_id)
        update_movie.cinema_hall = update_hall

    update_movie.save()
    return update_movie


def delete_movie_session_by_id(session_id: int) -> None:
    delete_movie = MovieSession.objects.get(id=session_id)
    delete_movie.delete()
