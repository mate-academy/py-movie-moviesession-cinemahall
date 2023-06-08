from typing import List, Optional

from db.models import Movie
from django.db.models import QuerySet


def get_movies(
        genres_ids: Optional[List[int]] = None,
        actors_ids: Optional[List[int]] = None,
) -> QuerySet:
    queryset = Movie.objects.all()
    if genres_ids:
        queryset = queryset.filter(
            genres__id__in=genres_ids
        )
    if actors_ids:
        queryset = queryset.filter(
            actors__id__in=actors_ids
        )
    return queryset


def get_movie_by_id(movie_id: int) -> Movie:
    queryset = Movie.objects.all()
    queryset = queryset.get(id=movie_id)
    return queryset


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: Optional[List[int]] = None,
        actors_ids: Optional[List[int]] = None,
) -> Movie:
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        new_movie.genres.set(genres_ids)

    if actors_ids:
        new_movie.actors.set(actors_ids)

    return new_movie
