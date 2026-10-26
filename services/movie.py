from typing import Optional
from django.db.models import QuerySet

from db.models import Movie


def get_movies(
        genres_ids: Optional[list[int]] = None,
        actors_ids: Optional[list[int]] = None
) -> QuerySet[Movie]:
    """
    Returns movies filtered by genres and/or actors.

    If both genres_ids and actors_ids are provided, returns movies that have
    at least one genre from genres_ids AND at least one actor from actors_ids.

    :param genres_ids: List of genre IDs (optional)
    :param actors_ids: List of actor IDs (optional)
    :return: QuerySet of movies
    """
    queryset = Movie.objects.all()

    if genres_ids is not None:
        queryset = queryset.filter(genres__id__in=genres_ids)

    if actors_ids is not None:
        queryset = queryset.filter(actors__id__in=actors_ids)

    return queryset.distinct()


def get_movie_by_id(movie_id: int) -> Movie:
    """
    Returns a movie by ID.

    :param movie_id: Movie ID
    :return: Movie object
    """
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: Optional[list[int]] = None,
        actors_ids: Optional[list[int]] = None
) -> Movie:
    """
    Creates a new movie with title, description, genres and actors.

    :param movie_title: Movie title
    :param movie_description: Movie description
    :param genres_ids: List of genre IDs (optional)
    :param actors_ids: List of actor IDs (optional)
    :return: Created Movie object
    """
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    if genres_ids is not None:
        movie.genres.set(genres_ids)

    if actors_ids is not None:
        movie.actors.set(actors_ids)

    return movie
