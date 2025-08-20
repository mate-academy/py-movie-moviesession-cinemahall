from db.models import MovieSession, Movie, CinemaHall

def create_movie_session(
        movie_show_time,
        movie_id: int,
        cinema_hall_id: int
) -> CinemaHall:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie=Movie.objects.get(id=movie_id),
        cinema_hall=CinemaHall.objects.get(id=cinema_hall_id),
    )

def get_movies_sessions(session_date=None) -> List[MovieSession]:
    qs = MovieSession.objects.all()
    if session_date:
        # session_date в формате "YYYY-MM-DD"
        return qs.filter(show_time__date=session_date)
    return qs

def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)

def update_movie_session(
        session_id: int,
        show_time=None,
        movie_id=None,
        cinema_hall_id=None
) -> CinemaHall:
    session = MovieSession.objects.get(id=session_id)
    if show_time is not None:
        session.show_time = show_time
    if movie_id is not None:
        session.movie = Movie.objects.get(id=movie_id)
    if cinema_hall_id is not None:
        session.cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    session.save()
    return session

def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
