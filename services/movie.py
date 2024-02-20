from django.db.models import QuerySet

import init_django_orm  # noqa:F401

from db.models import Movie


def get_movies(genres_ids: list[int] = None,
               actors_ids: list[int] = None
               ) -> QuerySet:
    movies = Movie.objects.all()

    if genres_ids:
        movies = movies.filter(genres__id__in=genres_ids)

    if actors_ids:
        movies = movies.filter(actors__id__in=actors_ids)
    return movies


def get_movie_by_id(movie_id: int) -> Movie:
    movie = Movie.objects.get(id=movie_id)
    return movie


def create_movie(movie_title: str,
                 movie_description: str,
                 actors_ids: list[int] = None,
                 genres_ids: list[int] = None,
                 ) -> None:
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )

    if actors_ids:
        new_movie.actors.set(actors_ids)

    if genres_ids:
        new_movie.genres.set(genres_ids)
