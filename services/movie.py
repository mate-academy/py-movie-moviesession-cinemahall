# services/movie.py
from typing import Iterable, Optional, Sequence

from db.models import Movie
from django.db.models import QuerySet


def get_movies(
    genres_ids: Optional[Sequence[int]] = None,
    actors_ids: Optional[Sequence[int]] = None,
) -> QuerySet[Movie]:
    qs = Movie.objects.all()
    if genres_ids:
        qs = qs.filter(genres__id__in=list(genres_ids))
    if actors_ids:
        qs = qs.filter(actors__id__in=list(actors_ids))
    return qs.distinct()


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
        movie.genres.add(*list(genres_ids))
    if actors_ids:
        movie.actors.add(*list(actors_ids))
    return movie
