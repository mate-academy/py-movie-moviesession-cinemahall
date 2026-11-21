from db.models import Movie
from typing import Any


def get_movies(
    genres_ids: list[int] | None = None,
    actors_ids: list[int] | None = None
) -> Any:
    movies = Movie.objects.all()
    if genres_ids is not None:
        movies = movies.filter(genres__id__in=genres_ids)
    if actors_ids is not None:
        movies = movies.filter(actors__id__in=actors_ids)
    return movies.distinct()


def get_movie_by_id(movie_id: int) -> Any:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str,
                 movie_description: str | None,
                 genres_ids: list[int] | None = None,
                 actors_ids: list[int] | None = None) -> Any:

    movie = Movie.objects.create(title=movie_title,
                                 description=movie_description)
    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)

    return movie
