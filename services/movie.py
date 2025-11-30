from django.db.models import QuerySet

from db.models import Movie
from typing import Optional


def get_movies(genres_ids: Optional[list[int]],
               actors_ids: Optional[list[int]]) -> QuerySet[Movie]:
    if not genres_ids and not actors_ids:
        return Movie.objects.all()
    if genres_ids and actors_ids:
        return Movie.objects.filter(genres__id__in=genres_ids,
                                    actors__id__in=actors_ids)
    if genres_ids and not actors_ids:
        return Movie.objects.filter(genres__id__in=genres_ids)
    if not genres_ids and actors_ids:
        return Movie.objects.filter(actors__id__in=actors_ids)


def get_movie_by_id(id: int) -> Movie:
    return Movie.objects.get(id=id)


def create_movie(movie_title: str, movie_description: str,
                 genres_ids: Optional[list[int]],
                 actors_ids: Optional[list[int]]) -> Movie:
    return Movie.objects.create(title=movie_title,
                                description=movie_description,
                                genres__id__in=genres_ids,
                                actors__id__in=actors_ids)
