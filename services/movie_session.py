from time import strptime

from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(
        movie_show_time,
        cinema_hall_id,
        movie_id
):
    MovieSession.objects.create(
        show_time=movie_show_time,
        movie=Movie.objects.get(id=movie_id),
        cinema_hall=CinemaHall.objects.get(id=cinema_hall_id)
    )


def get_movies_sessions(session_date: str = None):
    movies = MovieSession.objects.all()
    if session_date is not None:
        movies = movies.filter(show_time__date=session_date)
    else:
        movies = movies.all()
    return movies


def get_movie_session_by_id(search_id):
    queryset = MovieSession.objects.get(id=search_id)
    return queryset


def update_movie_session(
        session_id,
        show_time=None,
        movie_id=None,
        cinema_hall_id=None
):
    queryset = MovieSession.objects.get(id=session_id)

    if show_time is not None:
        queryset.show_time = show_time
    if movie_id is not None:
        queryset.movie = Movie.objects.get(id=movie_id)
    if cinema_hall_id is not None:
        queryset.cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    queryset.save()


def delete_movie_session_by_id(session_id):
    queryset = MovieSession.objects.get(id=session_id)
    queryset.delete()
