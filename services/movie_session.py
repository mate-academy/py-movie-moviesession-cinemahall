from db.models import MovieSession


def create_movie_session(movie_show_time, movie_id: int, cinema_hall_id: int):
    new_movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )

    return new_movie_session


def get_movies_sessions(session_date: str = None):
    queryset = MovieSession.objects.all()
    if session_date:
        queryset = queryset.filter(show_time__date=session_date)

    return queryset


def get_movie_session_by_id(movie_session_id: int):
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time=None,
        movie_id: int = None,
        cinema_hall_id: int = None):
    queryset = MovieSession.objects.all()

    if show_time and movie_id and cinema_hall_id:
        queryset.filter(id=session_id).update(
            show_time=show_time,
            movie=movie_id,
            cinema_hall=cinema_hall_id
        )

    if show_time and movie_id and not cinema_hall_id:
        queryset.filter(id=session_id).update(
            show_time=show_time,
            movie=movie_id
        )

    if show_time and not movie_id and cinema_hall_id:
        queryset.filter(id=session_id).update(
            show_time=show_time,
            cinema_hall=cinema_hall_id
        )

    if not show_time and movie_id and cinema_hall_id:
        queryset.filter(id=session_id).update(
            movie=movie_id,
            cinema_hall=cinema_hall_id
        )

    if show_time and not movie_id and not cinema_hall_id:
        queryset.filter(id=session_id).update(
            show_time=show_time
        )

    if not show_time and movie_id and not cinema_hall_id:
        queryset.filter(id=session_id).update(
            movie=movie_id
        )

    if not show_time and not movie_id and cinema_hall_id:
        queryset.filter(id=session_id).update(
            cinema_hall=cinema_hall_id
        )


def delete_movie_session_by_id(session_id: int):
    queryset = MovieSession.objects.all()
    queryset.filter(id=session_id).delete()
