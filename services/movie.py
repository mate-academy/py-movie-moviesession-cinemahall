from django.db import models

from db.models import Movie


def get_movies(
        genres_ids: list = None,
        actors_ids: list = None
) -> models.QuerySet:

    movies = Movie.objects.all()
    if genres_ids:
        movies = movies.filter(genre__id__in=genres_ids)
    if actors_ids:
        movies = movies.filter(actor__id__in=actors_ids)
    return movies


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        title: str,
        description: str,
        genres_ids: list = None,
        actors_isd: list = None
) -> Movie:

    movie = Movie.objects.create(title=title, description=description)
    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_isd:
        movie.actors.set(actors_isd)
    return movie
