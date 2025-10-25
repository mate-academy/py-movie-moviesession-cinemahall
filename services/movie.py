from __future__ import annotations
from typing import Any

from db.models import Movie


def get_movies(genres_ids: list = None,
               actors_ids: list = None
               ) -> Any | None:
    if not genres_ids and not actors_ids:
        return Movie.objects.all()

    if genres_ids and actors_ids:
        queryset = Movie.objects.filter(
            genres__id__in=genres_ids,
            actors__id__in=actors_ids)
        return queryset.distinct()

    if genres_ids and not actors_ids:
        movies = Movie.objects.filter(
            genres__id__in=genres_ids
        )
        return movies

    if actors_ids and not genres_ids:
        movies = Movie.objects.filter(
            actors__id__in=actors_ids
        )
        return movies


def get_movie_by_id(movie_id: int) -> Movie | None:
    movie = Movie.objects.get(id=movie_id)
    if movie:
        return movie
    return None


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: list = None,
                 actors_ids: list = None,
                 ) -> None:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    movie.genres.set(genres_ids) if genres_ids else None
    movie.actors.set(actors_ids) if actors_ids else None
