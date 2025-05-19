from django.db.models import QuerySet
from datetime import datetime
from typing import Optional
from db.models import MovieSession

def create_movie_session(
  movie_show_time: datetime,
  movie_id: int,
  cinema_hall_id: int
) -> MovieSession:
  return MovieSession.objects.create(
    show_time=movie_show_time,
    cinema_hall=cinema_hall_id,
    movie=movie_id
  )
  
def get_movies_sessions(session_date: Optional[str] = None) -> QuerySet:
  queryset = MovieSession.objects.all()
  try:
    if session_date:
      date_obj = datetime.strptime(session_date, "%Y-%m-%d").date()
      queryset = queryset.filter(show_time__date=date_obj)
  except ValueError:
    raise ValueError("Invalid date format. Use 'YYYY-MM-DD'.")
  return queryset

def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
  return MovieSession.objects.get(id=movie_session_id)

def update_movie_session(
  session_id: int,
  show_time: datetime = None,
  movie_id: int = None,
  cinema_hall_id: int = None
) -> MovieSession:
  movie_to_update = MovieSession.objects.get(id=session_id)
  if show_time:
    movie_to_update.show_time = show_time
  if movie_id:
    movie_to_update.movie = Movie.objects.get(id=movie_id)
  if cinema_hall_id:
    movie_to_update.cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
  movie_to_update.save()
  return movie_to_update

def delete_movie_session_by_id(session_id: int) -> None:
  movie_to_delete = MovieSession.objects.get(id=session_id)
  movie_to_delete.delete()
  
