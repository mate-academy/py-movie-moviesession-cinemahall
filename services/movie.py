from django.db.models import QuerySet

from db.models import Movie, Actor, Genre
from services.serv_support import (ids_are_corrects_and_exist)


def get_movies(genres_ids: list[int] | None = None,
               actors_ids: list[int] | None = None) -> QuerySet:
    query = Movie.objects.all()
    if ids_are_corrects_and_exist(genres_ids, Genre):
        query = query.filter(genres__id__in=genres_ids)
    if ids_are_corrects_and_exist(actors_ids, Actor):
        query = query.filter(actors__id__in=actors_ids)
    return query


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str, movie_description: str,
                 genres_ids: list[int] | None = None,
                 actors_ids: list[int] | None = None) -> Movie:
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if ids_are_corrects_and_exist(actors_ids, Actor):
        new_movie.actors.set(actors_ids)
    if ids_are_corrects_and_exist(genres_ids, Genre):
        new_movie.genres.set(genres_ids)
    return new_movie
