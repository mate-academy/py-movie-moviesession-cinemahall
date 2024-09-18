from django.db.models import QuerySet

from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)

    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=cinema_hall,
        movie=movie
    )


def get_movies_sessions(session_date: str = None) -> QuerySet:
    queryset = MovieSession.objects.all()

    if session_date:
        year, month, day = map(int, session_date.split("-"))

        queryset = queryset.filter(show_time__year=year)
        queryset = queryset.filter(show_time__month=month)
        queryset = queryset.filter(show_time__day=day)

    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    if show_time:
        MovieSession.objects.filter(id=session_id).update(show_time=show_time)
    if movie_id:
        new_movie = Movie.objects.get(id=movie_id)
        MovieSession.objects.filter(id=session_id).update(movie=new_movie)
    if cinema_hall_id:
        new_cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
        MovieSession.objects.filter(
            id=session_id).update(cinema_hall=new_cinema_hall)


def delete_movie_session_by_id(movie_session_id: int) -> None:
    get_movie_session_by_id(movie_session_id).delete()
