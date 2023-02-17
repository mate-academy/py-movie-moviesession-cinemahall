from typing import Optional

from django.db.models import QuerySet
from db.models import Movie
from django.shortcuts import get_object_or_404


def get_movies(
        genres_ids: Optional[list[int]] = None,
        actors_ids: Optional[list[int]] = None
) -> QuerySet:
    queryset = Movie.objects.all()
    if genres_ids and actors_ids:
        queryset = queryset.filter(
            genres__id__in=genres_ids, actors__id__in=actors_ids
        )
    elif genres_ids:
        queryset = queryset.filter(genres__id__in=genres_ids)
    elif actors_ids:
        queryset = queryset.filter(actors__id__in=actors_ids)
    return queryset


def get_movie_by_id(movie_id: int) -> Movie:
    return get_object_or_404(Movie, id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: Optional[list[int]] = None,
        actors_ids: Optional[list[int]] = None
) -> QuerySet:

    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    if genres_ids:
        new_movie.genres.set(genres_ids)
    if actors_ids:
        new_movie.actors.set(actors_ids)

    return new_movie
