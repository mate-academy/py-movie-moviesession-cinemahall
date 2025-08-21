from typing import List, Optional
from db.models import Movie
from django.db.models import QuerySet


def get_movies(
        genres_ids: Optional[List[int]] = None,
        actors_ids: Optional[List[int]] = None,
) -> QuerySet:

    if genres_ids is None and actors_ids is None:
        return Movie.objects.all()
    elif genres_ids and actors_ids:
        return Movie.objects.filter(
            genres__in=genres_ids,
            actors__in=actors_ids
        )
    elif genres_ids:
        return Movie.objects.filter(genres__in=genres_ids)
    elif actors_ids:
        return Movie.objects.filter(actors__in=actors_ids)


def get_movie_by_id(movie_id: int) -> QuerySet:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: Optional[List[int]] = None,
        actors_ids: Optional[List[int]] = None,
) -> None:

    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description)
    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)
