import init_django_orm  # noqa: F401

from db.models import Movie
from django.db.models.query import QuerySet

from typing import Optional


def get_movies(
        genres_ids: Optional[list[int]] = None,
        actors_ids: Optional[list[int]] = None
) -> QuerySet:
    movies = Movie.objects.all()

    if not genres_ids and not actors_ids:
        return movies
    elif genres_ids and actors_ids:
        return movies.filter(genres__id__in=genres_ids).filter(
            actors__id__in=actors_ids
        )
    elif genres_ids:
        return movies.filter(genres__id__in=genres_ids)
    elif actors_ids:
        return movies.filter(actors__id__in=actors_ids)


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
    movie_title: str,
    movie_description: str,
    genres_ids: Optional[list[int]] = None,
    actors_ids: Optional[list[int]] = None,
) -> Movie:

    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if actors_ids:
        movie.actors.set(actors_ids)
    if genres_ids:
        movie.genres.set(genres_ids)

    return movie
