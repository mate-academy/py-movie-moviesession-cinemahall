from django.db.models import QuerySet

from typing import Optional
from db.models import Movie, Genre, Actor


def get_movies(
    genres_ids: Optional[list[int]] = None,
    actors_ids: Optional[list[int]] = None
) -> QuerySet:
    if not genres_ids and not actors_ids:
        return Movie.objects.all()

    if not genres_ids:
        return Movie.objects.filter(actors__in=actors_ids).distinct()

    if not actors_ids:
        return Movie.objects.filter(genres__in=genres_ids).distinct()

    return Movie.objects.filter(
        genres__id__in=genres_ids
    ).filter(
        actors__id__in=actors_ids
    ).distinct()


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
    movie_title: str,
    movie_description: str,
    genres_ids: Optional[list[int]] = None,
    actors_ids: Optional[list[int]] = None
) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    if genres_ids:
        genres = Genre.objects.filter(id__in=genres_ids)
        movie.genres.add(*genres)

    if actors_ids:
        actors = Actor.objects.filter(id__in=actors_ids)
        movie.actors.add(*actors)

    return movie
