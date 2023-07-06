import init_django_orm  # noqa: F401

from typing import List
from django.db.models import QuerySet

from db.models import Movie


def get_movies(
        genres_ids: List[int] = None,
        actors_ids: List[int] = None
) -> QuerySet:
    queryset = Movie.objects.all()

    if genres_ids and actors_ids:
        queryset = queryset.filter(
            actors__id__in=actors_ids,
            genres__id__in=genres_ids
        )
    elif genres_ids and actors_ids is None:
        queryset = queryset.filter(genres__id__in=genres_ids)
    elif genres_ids is None and actors_ids:
        queryset = queryset.filter(actors__id__in=actors_ids)

    return queryset


def get_movie_by_id(movie_id: int) -> QuerySet:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: List[int] = None,
        actors_ids: List[int] = None,
) -> None:
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    if genres_ids is not None:
        new_movie.genres.set(genres_ids)

    if actors_ids is not None:
        new_movie.actors.set(actors_ids)
