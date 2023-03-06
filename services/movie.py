from typing import Union, List

from db.models import Movie
from django.db.models.query import QuerySet


def get_movies(
        genres_ids: Union[List[int], None] = None,
        actors_ids: Union[List[int], None] = None
) -> QuerySet:
    query_set = Movie.objects.all()

    if genres_ids:
        query_set = query_set.filter(genres__id__in=genres_ids)

    if actors_ids:
        query_set = query_set.filter(actors__id__in=actors_ids)

    return query_set


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: Union[List[int], None] = None,
        actors_ids: Union[List[int], None] = None,
) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)

    return movie
