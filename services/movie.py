from typing import List
from django.db import IntegrityError
from django.db.models.query import QuerySet
from db.models import Movie


def get_movies(
        genres_ids: List[int] = None,
        actors_ids: List[int] = None
) -> QuerySet:
    queryset = Movie.objects.all()
    if genres_ids is not None:
        queryset = queryset.filter(genres__id__in=genres_ids)
    if actors_ids is not None:
        queryset = queryset.filter(actors__id__in=actors_ids)
    return queryset.distinct()  # unique values


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: List[int] = None,
        actors_ids: List[int] = None
) -> None:
    movie, is_created = Movie.objects.get_or_create(
        title=movie_title,
        description=movie_description
    )

    if genres_ids is not None:
        try:
            movie.genres.add(
                *genres_ids
            )
        except IntegrityError as e:
            print(f"Wrong Genre id: {e}")
    if actors_ids is not None:
        try:
            movie.actors.add(
                *actors_ids
            )
        except IntegrityError as e:
            print(f"Wrong Actor id: {e}")
