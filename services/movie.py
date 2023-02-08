from db.models import Movie
from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from typing import Optional


def get_movies(
        genres_ids: Optional[list[int]] = None,
        actors_ids: Optional[list[int]] = None
) -> QuerySet:
    queryset = Movie.objects.all()
    if genres_ids and actors_ids:
        return queryset.filter(
            genres__id__in=genres_ids,
            actors__id__in=actors_ids
        )

    if genres_ids:
        return queryset.filter(genres__id__in=genres_ids)

    if actors_ids:
        return queryset.filter(actors__id__in=actors_ids)

    return queryset


def get_movie_by_id(movie_id: int) -> Movie:
    return get_object_or_404(Movie, id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: Optional[list[int]] = None,
        actors_ids: Optional[list[int]] = None
) -> None:
    new_film = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )

    if genres_ids:
        new_film.genres.set(genres_ids)
    if actors_ids:
        new_film.actors.set(actors_ids)
