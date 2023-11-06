from typing import List
from django.db.models import QuerySet
from db.models import Movie


def get_movies(genres_ids: List[int] = None,
               actors_ids: List[int] = None) -> QuerySet:

    movies_queryset = Movie.objects.all()

    if genres_ids:
        movies_queryset = movies_queryset.filter(genres__id__in=genres_ids)
    if actors_ids:
        movies_queryset = movies_queryset.filter(actors__id__in=actors_ids)

    return movies_queryset


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: List[int] = None,
                 actors_ids: List[int] = None) -> None:

    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    if genres_ids:
        new_movie.genres.set(genres_ids)
    if actors_ids:
        new_movie.actors.set(actors_ids)
