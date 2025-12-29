from django.shortcuts import get_object_or_404
from django.utils import timezone
from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(movie_show_time, movie_id, cinema_hall_id):
    """
    Creates a new movie session with the provided parameters.
    """
    movie = get_object_or_404(Movie, id=movie_id)
    cinema_hall = get_object_or_404(CinemaHall, id=cinema_hall_id)
    movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie=movie,
        cinema_hall=cinema_hall
    )
    return movie_session


def get_movies_sessions(session_date=None):
    """
    Returns all movie sessions,
    or movie sessions for a specific date if provided.
    """
    queryset = MovieSession.objects.all()
    if session_date:
        try:
            year, month, day = map(int, session_date.split('-'))
            date_obj = timezone.datetime(year, month, day).date()
            queryset = queryset.filter(show_time__date=date_obj)
        except ValueError:
            # Handle invalid date format,
            # maybe log an error or return an empty queryset
            return MovieSession.objects.none()
    return queryset


def get_movie_session_by_id(movie_session_id):
    """
    Returns a movie session by its ID.
    """
    try:
        return MovieSession.objects.get(id=movie_session_id)
    except MovieSession.DoesNotExist:
        return None


def update_movie_session(
        session_id,
        show_time=None,
        movie_id=None,
        cinema_hall_id=None):
    """
    Updates a movie session with the provided ID and optional fields.
    """
    try:
        movie_session = MovieSession.objects.get(id=session_id)
    except MovieSession.DoesNotExist:
        return None

    if show_time is not None:
        movie_session.show_time = show_time
    if movie_id is not None:
        movie = get_object_or_404(Movie, id=movie_id)
        movie_session.movie = movie
    if cinema_hall_id is not None:
        cinema_hall = get_object_or_404(CinemaHall, id=cinema_hall_id)
        movie_session.cinema_hall = cinema_hall

    movie_session.save()
    return movie_session


def delete_movie_session_by_id(session_id):
    """
    Deletes a movie session by its ID.
    """
    try:
        movie_session = MovieSession.objects.get(id=session_id)
        movie_session.delete()
        return True  # Indicate successful deletion
    except MovieSession.DoesNotExist:
        return False  # Indicate that the session was not found
