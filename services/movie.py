from typing import Any
from db.models import Actor, Genre, Movie
from django.core.exceptions import ObjectDoesNotExist


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> Movie:
    queryset = Movie.objects.all()

    if genres_ids:
        queryset = queryset.filter(genres__id__in=genres_ids)

    if actors_ids:
        queryset = queryset.filter(actors__id__in=actors_ids)

    return queryset.distinct()


def get_movie_by_id(movie_id: int) -> Any:
    try:
        return Movie.objects.get(id=movie_id)
    except ObjectDoesNotExist as error:
        return error


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None,
) -> Any:

    movie, created = Movie.objects.get_or_create(
        title=movie_title,
        description=movie_description,
    )
    if actors_ids:
        actors = Actor.objects.filter(id__in=actors_ids)
        movie.actors.set(actors)

    if genres_ids:
        genres = Genre.objects.filter(id__in=genres_ids)
        movie.genres.set(genres)
