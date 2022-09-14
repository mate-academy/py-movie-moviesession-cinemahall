from typing import List
import init_django_orm  # noqa: F401
from db.models import Movie


def get_movies(genres_ids=None, actors_ids=None):
    movies = Movie.objects.all()
    if genres_ids is not None:
        movies = movies.filter(genres__id__in=genres_ids)
    if actors_ids is not None:
        movies = movies.filter(actors__id__in=actors_ids)
    return movies


def get_movie_by_id(movie_id: int):
    return Movie.objects.get(pk=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: List[int] = None,
                 actors_ids: List[int] = None):
    movie = Movie.objects.create(title=movie_title,
                                 description=movie_description)
    if genres_ids is not None:
        movie.genres.set(genres_ids)
    if actors_ids is not None:
        movie.actors.set(actors_ids)
