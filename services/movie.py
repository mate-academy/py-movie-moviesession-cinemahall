from db.models import Movie
from django.db.models import QuerySet
from typing import List, Optional


def get_movies(
    genres_ids: Optional[List[int]] = None,
    actors_ids: Optional[List[int]] = None
) -> QuerySet:
    query = Movie.objects.all()
    if actors_ids is not None:
        query = query.filter(actors__id__in=actors_ids)
    if genres_ids is not None:
        query = query.filter(genres__id__in=genres_ids)
    return query


def get_movie_by_id(movie_id: int) -> QuerySet:
    return Movie.objects.get(id=movie_id)


def create_movie(
    movie_title: str,
    movie_description: str,
    genres_ids: Optional[List[int]] = None,
    actors_ids: Optional[List[int]] = None,
) -> Movie:
    movie = Movie.objects.create(
        title=movie_title, description=movie_description
    )
    if genres_ids is not None:
        movie.genres.set(genres_ids)
    if actors_ids is not None:
        movie.actors.set(actors_ids)
    return movie
