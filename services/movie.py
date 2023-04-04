from django.db.models import QuerySet
from typing import Optional

from db.models import Movie


def get_movies(genres_ids: Optional[list[int]] = None,
               actors_ids: Optional[list[int]] = None) -> QuerySet:

    queryset = Movie.objects.all()

    if genres_ids and actors_ids:
        queryset = queryset.filter(genres__id__in=genres_ids
                                   ).filter(actors__id__in=actors_ids)

    if actors_ids is None and genres_ids:
        queryset = queryset.filter(genres__id__in=genres_ids)

    if genres_ids is None and actors_ids:
        queryset = queryset.filter(actors__id__in=actors_ids)

    return queryset


def get_movie_by_id(movie_id: id) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: Optional[list[int]] = None,
                 actors_ids: Optional[list[int]] = None) -> None:

    new_movie = Movie.objects.create(title=movie_title,
                                     description=movie_description)

    if genres_ids:
        new_movie.genres.set(genres_ids)

    if actors_ids:
        new_movie.actors.set(actors_ids)
