from typing import List

from django.db.models import QuerySet

from db.models import Movie


def get_movies(genres_ids: List[int] = None, actors_ids: List[int] = None) -> QuerySet:
    queryset = Movie.objects.all()

    if genres_ids is not None:
        queryset = queryset.filter(genres__id__in=genres_ids)

    if actors_ids is not None:
        queryset = queryset.filter(actors__id__in=genres_ids)

    return queryset


def get_movie_by_id(movie_id: int) -> QuerySet:
    return Movie.objects.filter(movie_id=movie_id)
