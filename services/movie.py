from django.db.models import QuerySet

from db import models


def get_movies(genres_ids: list = None, actors_ids: list = None) -> QuerySet:
    query_set = models.Movie.objects.all()
    if not genres_ids and not actors_ids:
        return query_set
    if genres_ids:
        query_set = query_set.filter(genres__in=genres_ids).distinct()
    if actors_ids:
        query_set = query_set.filter(actors__in=actors_ids).distinct()
    return query_set


def get_movie_by_id(movie_id: int) -> models.Movie:
    return models.Movie.objects.get(id=movie_id)


def create_movie(
        genres_ids: list = None,
        actors_ids: list = None,
        movie_title: str = None,
        movie_description: str = None
) -> None:
    new_movie = models.Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        new_movie.genres.add(*genres_ids)
    if actors_ids:
        new_movie.actors.add(*actors_ids)
