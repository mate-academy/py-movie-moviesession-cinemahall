from typing import List, Optional
from django.db.models import QuerySet
from db.models import Movie, Genre, Actor


def get_movies(
    genres_ids: Optional[List[int]] = None,
    actors_ids: Optional[List[int]] = None
) -> QuerySet[Movie]:
    """
    Retrieve movies filtered by genres and/or actors.

    Args:
        genres_ids (Optional[List[int]]):
        A list of genre IDs to filter movies by.
        actors_ids (Optional[List[int]]):
        A list of actor IDs to filter movies by.

    Returns:
        QuerySet[Movie]: A QuerySet of Movie instances.
    """
    queryset = Movie.objects.all()
    if genres_ids:
        queryset = queryset.filter(
            genres__id__in=genres_ids
        ).distinct()
    if actors_ids:
        queryset = queryset.filter(
            actors__id__in=actors_ids
        ).distinct()
    return queryset


def get_movie_by_id(movie_id: int) -> Optional[Movie]:
    """
    Retrieve a movie by its ID.

    Args:
        movie_id (int): The ID of the movie to retrieve.

    Returns:
        Optional[Movie]: The Movie instance if found, otherwise None.
    """
    try:
        return Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        return None


def create_movie(
    movie_title: str,
    movie_description: str,
    genres_ids: Optional[List[int]] = None,
    actors_ids: Optional[List[int]] = None
) -> Movie:
    """
    Create a new movie and save it to the database.

    Args:
        movie_title (str):
        The title of the movie.
        movie_description (str):
        The description of the movie.
        genres_ids (Optional[List[int]]):
        A list of genre IDs to associate with the movie.
        actors_ids (Optional[List[int]]):
        A list of actor IDs to associate with the movie.

    Returns:
        Movie: The created Movie instance.
    """
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    if genres_ids:
        genres = Genre.objects.filter(id__in=genres_ids)
        movie.genres.set(genres)

    if actors_ids:
        actors = Actor.objects.filter(id__in=actors_ids)
        movie.actors.set(actors)

    return movie
