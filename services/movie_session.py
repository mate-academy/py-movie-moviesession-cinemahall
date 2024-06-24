from datetime import datetime
from django.db.models import QuerySet
from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(movie_show_time: Movie, movie_id: Movie,
                         cinema_hall_id: CinemaHall) -> None:
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
        session_date_time = datetime.strptime(session_date, "%Y-%m-%d")
        queryset = queryset.filter(show_time__date=session_date_time)
    return queryset


def get_movie_session_by_id(movie_session_id: Movie) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: MovieSession,
                         show_time: MovieSession = None,
                         movie_id: Movie = None,
                         cinema_hall_id: CinemaHall = None) -> MovieSession:
    session = MovieSession.objects.get(id=session_id)

    if show_time:
        session.show_time = show_time
    if movie_id:
        movie = Movie.objects.get(id=movie_id)
        session.movie = movie
    if cinema_hall_id:
        cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
        session.cinema_hall = cinema_hall

    session.save()
    return session


def delete_movie_session_by_id(session_id: MovieSession) -> MovieSession:
    MovieSession.objects.filter(id=session_id).delete()
