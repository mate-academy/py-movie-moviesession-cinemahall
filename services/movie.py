from django.db.models import QuerySet
from db.models import Movie, Actor, Genre

from typing import List


def get_movies(
        genres_ids: List[Genre] = None,
        actors_ids: List[Actor] = None
) -> QuerySet:

    queryset = Movie.objects.all()
    if genres_ids:
        queryset = queryset.filter(genres__id__in=genres_ids)
    if actors_ids:
        queryset = queryset.filter(actors__id__in=actors_ids)
    return queryset


def get_movie_by_id(movie_id: Movie) -> QuerySet:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: List[Genre] = None,
        actors_ids: List[Actor] = None
) -> None:
    queryset = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        queryset.genres.set(genres_ids)
    if actors_ids:
        queryset.actors.set(actors_ids)
