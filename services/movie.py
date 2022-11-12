from typing import List

from db.models import Movie
from django.db.models import QuerySet


def get_movies(
        genres_ids: List[int] = None,
        actors_ids: List[int] = None
) -> QuerySet:
    movies_query_set = Movie.objects.all()

    if genres_ids:
        movies_query_set = movies_query_set.filter(genres__id__in=genres_ids)
    if actors_ids:
        movies_query_set = movies_query_set.filter(actors__id__in=actors_ids)
    return movies_query_set


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: List[int] = None,
        actors_ids: List[int] = None
) -> Movie:
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    if genres_ids:
        new_movie.genres.add(*genres_ids)
    if actors_ids:
        new_movie.actors.add(*actors_ids)

    return new_movie
