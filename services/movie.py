from typing import List, Optional

from django.db.models import QuerySet

from db.models import Movie


def get_movies(
        genres_ids: List[int] = None,
        actors_ids: List[int] = None
) -> QuerySet:
    if not genres_ids and not actors_ids:
        return Movie.objects.all()

    movies = Movie.objects.all()

    if actors_ids and genres_ids:
        return movies.filter(
            actors__id__in=actors_ids,
            genres__id__in=genres_ids
        )

    elif actors_ids:
        return movies.filter(actors__id__in=actors_ids)

    elif genres_ids:
        return movies.filter(genres__id__in=genres_ids)

    return movies


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(pk=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: Optional[List[int]] = None,
        actors_ids: Optional[List[int]] = None,
) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )

    if genres_ids:
        movie.genres.set(genres_ids)

    if actors_ids:
        movie.actors.set(actors_ids)

    return movie
