from typing import Optional
from db.models import MovieSession, Movie, CinemaHall
from django.utils.timezone import make_aware
from datetime import datetime
from django.db.models import QuerySet


def create_movie_session(
    movie_show_time: datetime,
    movie_id: int,
    cinema_hall_id: int,
) -> MovieSession:
    """Create a new movie session."""
    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    if not movie_show_time.tzinfo:
        movie_show_time = make_aware(movie_show_time)
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie=movie,
        cinema_hall=cinema_hall,
    )


def update_movie_session(
    session_id: int,
    show_time: Optional[datetime] = None,
    movie_id: Optional[int] = None,
    cinema_hall_id: Optional[int] = None,
) -> MovieSession:
    """Update an existing movie session."""
    session = MovieSession.objects.get(id=session_id)
    if show_time:
        session.show_time = (
            make_aware(show_time) if not show_time.tzinfo else show_time
        )
    if movie_id:
        session.movie = Movie.objects.get(id=movie_id)
    if cinema_hall_id:
        session.cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    session.save()
    return session


def get_movie_sessions(
    session_date: Optional[str] = None,
) -> QuerySet[MovieSession]:
    """Retrieve movie sessions, optionally filtered by date."""
    if session_date:
        return MovieSession.objects.filter(
            show_time__date=session_date,
        )
    return MovieSession.objects.all()


def get_movie_session_by_id(session_id: int) -> MovieSession:
    """Retrieve a movie session by its ID."""
    return MovieSession.objects.get(id=session_id)


def delete_movie_session_by_id(session_id: int) -> None:
    """Delete a movie session by its ID."""
    session = MovieSession.objects.get(id=session_id)
    session.delete()
