from __future__ import annotations

from db.models import Movie, Genre, Actor

from django.db.models import QuerySet

from django.core.exceptions import ObjectDoesNotExist


def get_movies(
        genres_ids: list | None = None,
        actors_ids: list | None = None
) -> QuerySet:
    movies = Movie.objects.all()

    if genres_ids:
        movies = movies.filter(genres__in=genres_ids)

    if actors_ids:
        movies = movies.filter(actors__in=actors_ids)

    return movies


def get_movie_by_id(movie_id: int) -> Movie:
    try:
        movie = Movie.objects.get(id=movie_id)
        return movie
    except ObjectDoesNotExist:
        return None


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list | None = None,
        actors_ids: list | None = None
) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids is not None:
        genres = Genre.objects.filter(id__in=genres_ids)
        movie.genres.set(genres)

    if actors_ids is not None:
        actors = Actor.objects.filter(id__in=actors_ids)
        movie.actors.set(actors)

    movie.save()
    return movie
