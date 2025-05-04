from datetime import datetime

from django.db.models import QuerySet

from db.models import MovieSession

def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int
                         ) -> MovieSession:
    return MovieSession.objects.Creare(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )

def get_movies_sessions(session_date: datetime=None) -> QuerySet | MovieSession:
    if session_date:
        return MovieSession.objects.get(show_time__date=session_date)
    return MovieSession.objects.all()

def get_movie_session_by_id(movie_session_id) -> MovieSession:
    return MovieSession.objects.get(movie_session_id=movie_session_id)

def update_movie_session(session_id: int, /,
                               show_time: datetime=None,
                               movie_id: int=None,
                               cinema_hall_id: int=None) -> None:
    MovieSessionInstance = MovieSession.objects.get(session_id=session_id)
    if show_time:
        MovieSessionInstance.show_time=show_time
    if movie_id:
        MovieSessionInstance.movie_id = movie_id
    if cinema_hall_id:
        MovieSessionInstance.cinema_hall_id = cinema_hall_id
    MovieSessionInstance.save()


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(session_id=session_id).delete()