from django.db.models import QuerySet
from db.models import MovieSession, Movie, CinemaHall
from datetime import datetime


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int
                         ) -> MovieSession:
    return MovieSession.objects.create(show_time=movie_show_time,
                                       cinema_hall_id=cinema_hall_id,
                                       movie_id=movie_id)


def get_movies_sessions(session_date: str = None) -> QuerySet:
    queryset = MovieSession.objects.all()
    if session_date:
        date_show = datetime.strptime(session_date, "%Y-%m-%d").date()
        queryset = queryset.filter(show_time__date=date_show)
    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    movie_session_to_update = MovieSession.objects.get(id=session_id)
    if show_time:
        movie_session_to_update.show_time = show_time
    if movie_id:
        movie_session_to_update.movie = Movie.objects.get(id=movie_id)
    if cinema_hall_id:
        movie_session_to_update.cinema_hall = CinemaHall.objects.get(
            id=cinema_hall_id
        )
    return movie_session_to_update.save()


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
