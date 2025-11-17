# flake8: noqa: E402
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()


from db.models import Movie
from django.db.models.query import QuerySet


def get_movies(genres_ids: list = None, actors_ids: list = None) -> QuerySet:
    movies = Movie.objects.all()
    if genres_ids and actors_ids:
        movies = movies.filter(actors__id__in=actors_ids)
        return movies.filter(genres__id__in=genres_ids)
    elif actors_ids:
        return movies.filter(actors__id__in=actors_ids)
    elif genres_ids:
        return movies.filter(genres__id__in=genres_ids)
    return movies


def get_movie_by_id(movie_id: int) -> QuerySet:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list = None,
        actors_ids: list = None
) -> Movie:
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )

    if genres_ids:
        new_movie.genres.add(*genres_ids)

    if actors_ids:
        new_movie.actors.add(*actors_ids)

    return new_movie
