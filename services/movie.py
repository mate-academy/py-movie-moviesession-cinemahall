from typing import List

from django.db.models import QuerySet

from db.models import Movie


def get_movies(genres_ids: List[int], actors_ids: List[int]) -> QuerySet[Movie]:
    movies = Movie.objects.all()
    if not genres_ids and not actors_ids:
        return movies

    if genres_ids and actors_ids:
        movies = movies.objects.filter(
            genres_id__in=genres_ids,
            actors_id__in=actors_ids
        )

    if genres_ids:
        movies = movies.filter(genres_id__in=genres_ids)

    if actors_ids:
        movies = movies.filter(actors_id__in=actors_ids)

    return movies


def get_movie_by_id(movie_id: int) -> str:
    movie = Movie.objects.get(movie_id=movie_id)
    return movie


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: List[int],
        actors_ids: List[int]
) -> Movie:
    new_movie = Movie.objects.create(title=movie_title, description=movie_description)
    new_movie.genres_id.set(genres_ids)
    new_movie.actors_id.set(actors_ids)
    return new_movie
