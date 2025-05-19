from django.db.models import QuerySet

from db.models import Movie

def get_movies(
  genres_ids: list[int] = None,
  actors_ids: list[int] = None
) -> QuerySet:
  queryset = Movie.objects.all()
  if genres_ids and actors_ids:
    queryset = queryset.filter(genres__id__in=genres_ids, actors__id__in=actors_ids)
  if actors_ids:
    queryset = queryset.filter(actors__id__in=actors_ids)
  if genres_ids:
    queryset = queryset.filter(genres__id__in=genres_ids)
  return queryset

def get_movie_by_id(movie_id: int) -> Movie:
  return Movie.objects.get(id=movie_id)

def create_movie(
  movie_title: str,
  movie_description: str,
  genres_ids: list[int] = None,
  actors_ids: list[int] = None
) -> Movie:
  new_movie = Movie.objects.create(movie_title, movie_description)
  if genres_ids:
    new_movie.add(genres_ids)
  if actors_ids:
    new_movie.add(actors_ids)
  
