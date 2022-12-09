from typing import List

from db.models import Movie


def get_movies(genres_ids: List[int] = None,
               actors_ids: List[int] = None) -> None:
    query_set = Movie.objects.all()

    if genres_ids is not None:
        query_set = query_set.filter(genres__id__in=genres_ids)

    if actors_ids is not None:
        query_set = query_set.filter(actors__id__in=actors_ids)

    return query_set


def get_movie_by_id(id_movie: int) -> Movie:
    return Movie.objects.get(id=id_movie)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: List[int] = None,
        actors_ids: List[int] = None) -> None:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    if genres_ids is not None:
        movie.genres.set(genres_ids)

    if actors_ids is not None:
        movie.actors.set(actors_ids)
