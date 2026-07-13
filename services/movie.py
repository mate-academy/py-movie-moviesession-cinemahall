from typing import List
from django.db.models import QuerySet
from db.models import Movie


def create_movie(movie_title: str, movie_description: str,
                 genres_ids: List[int] = None,
                 actors_ids: List[int] = None) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)

    return movie


def get_movies(genres_ids: List[int] = None,
               actors_ids: List[int] = None) -> QuerySet[Movie]:

    movies = Movie.objects.all()

    if genres_ids is not None:
        movies = movies.filter(genres__in=genres_ids)
    if actors_ids is not None:
        movies = movies.filter(actors__in=actors_ids)
    if genres_ids is None and actors_ids is None:
        return movies
    return movies


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)
