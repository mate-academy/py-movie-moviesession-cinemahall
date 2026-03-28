from typing import List, Optional

from django.db.models.query import QuerySet

from db.models import Movie


def get_movies(
        genres_ids: Optional[List[int]] = None,
        actors_ids: Optional[List[int]] = None
) -> QuerySet:
    movies = Movie.objects.all()
    if genres_ids:
        movies = movies.filter(genres__in=genres_ids)
    if actors_ids:
        movies = movies.filter(actors__in=actors_ids)
    return movies


def get_movie_by_id(movie_pk: int) -> Movie:
    return Movie.objects.get(pk=movie_pk)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: Optional[List[int]] = None,
        actors_ids: Optional[List[int]] = None
) -> None:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)
