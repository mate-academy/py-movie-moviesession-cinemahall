from django.db.models.query import QuerySet
from typing import Optional

from db.models import Genre, Actor, Movie


def get_movies(
        genres_ids: Optional[list[int]] = None,
        actors_ids: Optional[list[int]] = None
) -> QuerySet[Movie]:

    queryset = Movie.objects.all()

    if genres_ids and actors_ids:
        queryset = queryset.filter(
            genres__id__in=genres_ids,
            actors__id__in=actors_ids
        ).distinct()

    if genres_ids:
        queryset = queryset.filter(genres__id__in=genres_ids)

    if actors_ids:
        queryset = queryset.filter(actors__id__in=actors_ids)
    return queryset


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: Optional[list[int]] = None,
        actors_ids: Optional[list[int]] = None,

) -> Movie:
    movi = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    if genres_ids:
        genres = Genre.objects.filter(id__in=genres_ids)
        movi.genres.set(genres)

    if actors_ids:
        actors = Actor.objects.filter(id__in=actors_ids)
        movi.actors.set(actors)

    return movi
