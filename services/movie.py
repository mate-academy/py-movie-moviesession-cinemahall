from typing import Optional
from db.models import Movie
from db.models import models


def get_movies(genres_ids: Optional[list[int]] = None,
               actors_ids: Optional[list[int]] = None) -> models.QuerySet:
    all_movies = Movie.objects.all()

    if genres_ids:
        all_movies = all_movies.filter(genres__id__in=genres_ids)

    if actors_ids:
        all_movies = all_movies.filter(actors__id__in=actors_ids)

    return all_movies


def get_movie_by_id(movie_id: int) -> models.QuerySet:
    return Movie.objects.get(id=movie_id)


def create_movie(
                 movie_title: str,
                 movie_description: str,
                 genres_ids: Optional[list[int]] = None,
                 actors_ids: Optional[list[int]] = None,
                 ) -> models.QuerySet:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)

    return movie
