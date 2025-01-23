from django.db.models import QuerySet

from db.models import CinemaHall, MoveSession, Movie


def get_cinema_halls() -> QuerySet:
    return CinemaHall.objects.all()

def create_cinema_hall(hall_name, hall_rows, hall_seats_in_row) -> CinemaHall:
    cinema_hall = CinemaHall.objects.create(
        name=hall_name,
        rows=hall_rows,
        seats_in_rows=hall_seats_in_row
    )

    return cinema_hall

def get_movie_sessions(session_date=None) -> QuerySet:
    if session_date:
        return CinemaHall.objects.filter(date__gte=session_date)
    return CinemaHall.objects.all()

def get_movie_session_by_id(movie_session_id):
    try:
        return MoveSession.objects.get(id=movie_session_id)
    except MoveSession.DoesNotExist:
        return None

def update_movie_session(session_id, show_time=None, movie_id=None, cinema_hall_id=None) -> MoveSession:
    try:
        movie_session = MoveSession.objects.get(id=session_id)
    except MoveSession.DoesNotExist:
        raise ValueError("Movie session with this ID does not exist")

    if show_time:
        movie_session.show_time = show_time
    if movie_id:
        movie_session.movie_id = Movie.objects.get(id=movie_id)
    if cinema_hall_id:
        movie_session.cinema_hall_id = CinemaHall.objects.get(id=cinema_hall_id)

    movie_session.save()


def delete_movie_session_by_id(session_id) -> None:
    try:
        movie_session = MoveSession.objects.get(id=session_id)
        movie_session.delete()
    except MoveSession.DoesNotExist:
        raise ValueError("Movie session with this ID does not exist")