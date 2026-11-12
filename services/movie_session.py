from django.db.models import QuerySet

from db.models import Movie, MovieSession, CinemaHall


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(pk=movie_session_id)


def get_movies_sessions(session_date: str = None) -> QuerySet[MovieSession]:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int,
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=CinemaHall.objects.get(pk=cinema_hall_id),
        movie=Movie.objects.get(pk=movie_id),
    )


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> MovieSession:
    updated_movie_session = MovieSession.objects.get(pk=session_id)
    if show_time:
        updated_movie_session.show_time = show_time
    if movie_id:
        updated_movie_session.movie = Movie.objects.get(pk=movie_id)
    if cinema_hall_id:
        updated_movie_session.cinema_hall = CinemaHall.objects.get(
            pk=cinema_hall_id
        )
    updated_movie_session.save()
    return updated_movie_session


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(pk=session_id).delete()
