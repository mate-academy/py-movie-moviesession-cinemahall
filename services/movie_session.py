import init_django_orm


from datetime import datetime, timedelta

from db.models import MovieSession


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id,
    )


def get_movies_sessions(session_date: str = None) -> MovieSession:
    queryset = MovieSession.objects.all()
    if session_date:
        _date = datetime.strptime(session_date, '%Y-%m-%d').date()
        queryset = queryset.filter(
            show_time__gt=_date,
            show_time__lt=_date + timedelta(days=1)
        )

    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None,
) -> None:
    movie_session = MovieSession.objects.get(id=session_id)

    if show_time:
        movie_session.show_time = show_time

    if movie_id:
        movie_session.movie_id = movie_id

    if cinema_hall_id:
        movie_session.cinema_hall_id = cinema_hall_id

    movie_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    movie_session = get_movie_session_by_id(session_id)
    movie_session.delete()

if __name__ == '__main__':
    pass