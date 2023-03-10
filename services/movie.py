from typing import List

from db.models import Movie


def get_movies(genres_ids: List[int] = None, actors_ids: List[int] = None):
    movie = Movie.objects.all()

    if genres_ids and actors_ids:
        movie = movie.filter(genres__id__in=genres_ids,
                             actors__id__in=actors_ids)

    if genres_ids and not actors_ids:
        movie = movie.filter(genres__id__in=genres_ids)

    if not genres_ids and actors_ids:
        movie = movie.filter(actors__id__in=actors_ids)

    return movie


def get_movie_by_id(movie_id: int):
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: List[int] = None,
        actors_ids: List[int] = None
):
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    if genres_ids:
        movie.genres.set(genres_ids)

    if actors_ids:
        movie.actors.set(actors_ids)
