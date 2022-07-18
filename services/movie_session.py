from db.models import MovieSession


def create_movie_session(movie_show_time, movie_id: int, cinema_hall_id):
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(session_date: str = None) -> list[MovieSession]:
    queryset = MovieSession.objects.all()

    if session_date:
        session_date_ = session_date.split("-")
        queryset = queryset.filter(
            show_time__year=session_date_[0],
            show_time__month=session_date_[1],
            show_time__day=session_date_[2]
        )

    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.filter(id=movie_session_id).get()


def update_movie_session(
        session_id: int,
        show_time=None,
        movie_id: int = None,
        cinema_hall_id: int = None
):
    queryset = MovieSession.objects.filter(id=session_id)
    if show_time:
        queryset.update(show_time=show_time)

    if movie_id:
        queryset.update(movie_id=movie_id)

    if cinema_hall_id:
        queryset.update(cinema_hall_id=cinema_hall_id)

    return queryset


def delete_movie_session_by_id(session_id: int):
    queryset = MovieSession.objects.filter(id=session_id).delete()
    return queryset
