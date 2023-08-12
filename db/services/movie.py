from typing import List

from django.db.models.query import QuerySet

# noinspection PyUnresolvedReferences
import init_django_orm
from db.models import Movie


def get_movies(
        genres_ids: List[int] = None,
        actors_ids: List[int] = None) -> QuerySet:
    queryset = Movie.objects.all()
    if genres_ids is not None:
        queryset = queryset.filter(genres__id__in=genres_ids)
    if actors_ids is not None:
        queryset = queryset.filter(actors__id__in=actors_ids)
    return queryset


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_id: List[int] = None,
        actors_ids: List[int] = None) -> Movie:
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_id is not None:
        new_movie.genres.add(
            genres_id
        )
    if actors_ids is not None:
        new_movie.actors.add(
            actors_ids
        )

# print(get_movies())
# print(get_movie_by_id(2))
create_movie("JoJo's Bizarre Adventure", "JOJO")