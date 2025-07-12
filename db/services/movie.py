from db.models import Movie
from typing import Any

def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> Any:
    queryset = Movie.objects.all()
    if genres_ids is not None:
        queryset = queryset.filter(genres__id__in=genres_ids)
    if actors_ids is not None:
        queryset = queryset.filter(actors__id__in=actors_ids)

    queryset = queryset.distinct()
    return queryset


def get_movie_by_id(movie_id: int) -> Any:
    return Movie.objects.get(id=movie_id)

def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None,
) -> Any:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    if genres_ids is not None:
        movie.genres.set(genres_ids)
    if actors_ids is not None:
        movie.actors.set(actors_ids)

    return movie
