from django.db.models import QuerySet
from db.models import Movie, Genre, Actor
from typing import Optional


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> Optional[QuerySet]:

    queryset = Movie.objects.all()

    if genres_ids:
        queryset = queryset.filter(genres__in=genres_ids)
    if actors_ids:
        queryset = queryset.filter(actors__in=actors_ids)

    return queryset.distinct()


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
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
