from datetime import datetime

from django.db.models import QuerySet

from db.models import MovieSession


def get_movies_sessions(session_date: str = None) -> QuerySet:
    queryset = MovieSession.objects.all()
    if session_date:
        date_object = datetime.strptime(session_date,
                                        "%Y-%m-%d").date()
        queryset = queryset.filter(show_time__date=date_object)

    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> MovieSession:
    movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )

    return movie_session


def update_movie_session(session_id: int,
                         show_time: datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> QuerySet[MovieSession]:
    movie_session = MovieSession.objects.filter(id=session_id)
    if movie_session:
        updates = {}
        if show_time:
            updates["show_time"] = show_time
        if movie_id:
            updates["movie_id"] = movie_id
        if cinema_hall_id:
            updates["cinema_hall_id"] = cinema_hall_id

        if updates:  # Only call update if there are fields to update
            movie_session.update(**updates)

    return movie_session

def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()