from typing import List

from db.models import Movie


def get_movies(genres_ids: List[int] = None, actors_ids: List[int] = None):
    queueset = Movie.objects.all()

    if genres_ids is not None:
        queueset = queueset.filter(genres__id__in=genres_ids)

    if actors_ids is not None:
        queueset = queueset.filter(actors__id__in=actors_ids)

    return queueset


def get_movie_by_id(movie_id: int):
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
):
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )

    if genres_ids is not None:
        new_movie.genres.set(genres_ids)

    if actors_ids is not None:
        new_movie.actors.set(actors_ids)

    return new_movie
