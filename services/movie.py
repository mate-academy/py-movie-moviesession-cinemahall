from db.models import Movie
from typing import List


def get_movies(genres_ids: List = None, actors_ids: List = None) -> Movie:
    queryset = Movie.objects.all()

    if genres_ids is not None and len(genres_ids) > 0:
        queryset = queryset.filter(genres__id__in=genres_ids)

    if actors_ids is not None and len(actors_ids) > 0:
        queryset = queryset.filter(actors__id__in=actors_ids)

    return queryset.distinct()


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str, movie_description: str,
        genres_ids: int = None, actors_ids: int = None) -> Movie:
    movie = Movie.objects.create(
        title=movie_title, description=movie_description)
    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)
    return movie
