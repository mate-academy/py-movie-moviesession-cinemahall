from typing import Iterable, Optional

from django.db.models import QuerySet

from db.models import Movie


def get_movies(
    genres_ids: Optional[Iterable[int]] = None,
    actors_ids: Optional[Iterable[int]] = None,
) -> QuerySet[Movie]:
    queryset = Movie.objects.all().order_by("id")

    if genres_ids:
        queryset = queryset.filter(genres__id__in=list(genres_ids))

    if actors_ids:
        queryset = queryset.filter(actors__id__in=list(actors_ids))

    return queryset.distinct().order_by("id")


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
    movie_title: str,
    movie_description: str,
    genres_ids: Optional[Iterable[int]] = None,
    actors_ids: Optional[Iterable[int]] = None,
) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )

    if genres_ids:
        movie.genres.set(list(genres_ids))

    if actors_ids:
        movie.actors.set(list(actors_ids))

    return movie
