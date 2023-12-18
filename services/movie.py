from typing import List

from django.db.models import QuerySet

from db.models import Movie


def get_movies(
        genres_ids: List[int] = None,
        actors_ids: List[int] = None
) -> QuerySet:
    queryset = Movie.objects.all()
    if genres_ids is not None and actors_ids is not None:
        queryset = queryset.filter(
            genres__in=genres_ids,
            actors__in=actors_ids
        ).distinct()
    if genres_ids is not None:
        queryset = queryset.filter(genres__in=genres_ids).distinct()
    if actors_ids is not None:
        queryset = queryset.filter(actors__in=actors_ids).distinct()
    return queryset


def get_movie_by_id(movie_id: int) -> QuerySet:
    movie = Movie.objects.get(pk=movie_id)
    return movie


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: List[int] = None,
        actors_ids: List[int] = None
) -> QuerySet:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    if genres_ids is not None:
        movie.genres.set(genres_ids)

    if actors_ids is not None:
        movie.actors.set(actors_ids)

    return movie
