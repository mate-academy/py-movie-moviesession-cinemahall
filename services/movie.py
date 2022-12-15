import init_django_orm  # noqa: F401
from typing import Any
from db.models import Movie
from django.db.models import QuerySet


def get_movies(genres_ids: list[int] = None,
               actors_ids: list[int] = None) -> QuerySet:
    query_movie = Movie.objects.all()

    if genres_ids is None and actors_ids is None:
        return query_movie

    elif genres_ids is not None and actors_ids is not None:
        return query_movie.filter(genres__in=genres_ids, actors__in=actors_ids)

    if genres_ids is not None:
        return query_movie.filter(genres__in=genres_ids)

    if actors_ids is not None:
        return query_movie.filter(actors__in=actors_ids)


def get_movie_by_id(movie_id: int) -> Any:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: list[int] = None,
                 actors_ids: list[int] = None) -> QuerySet:
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    if genres_ids is not None:
        new_movie.genres.set(genres_ids)

    if actors_ids is not None:
        new_movie.actors.set(actors_ids)

    return new_movie
