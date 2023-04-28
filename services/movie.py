from django.db.models import QuerySet

from db.models import Movie
from typing import Optional


def get_movies(
        genres_ids: Optional[list[int]] = None,
        actors_ids: Optional[list[int]] = None
) -> QuerySet:
    queryset = Movie.objects.all()

    if genres_ids:
        queryset = queryset.filter(genres__id__in=genres_ids)

    if actors_ids:
        queryset = queryset.filter(actors__id__in=actors_ids)

    return queryset


def get_movie_by_id(movie_id: int) -> QuerySet:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: Optional[list[int]] = None,
        actors_ids: Optional[list[int]] = None,
) -> None:
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    # if genres_ids is provided add genres to movies
    if genres_ids:
        new_movie.genres.set(genres_ids)
    # if actors_ids is provided add actors to movies
    if actors_ids:
        new_movie.actors.set(actors_ids)
