from typing import List, Optional
from db.models import Movie, Genre, Actor
from django.db.models import QuerySet
from django.core.exceptions import ObjectDoesNotExist


def get_movies(genres_ids: Optional[List[int]] = None,
               actors_ids: Optional[List[int]] = None) -> QuerySet:
    """
    Retrieve movies based on optional filters:
        genres_ids and actors_ids.

    If both filters are provided, return movies that match
        at least one genre and one actor.

    :param genres_ids: Optional list of genre IDs
    :param actors_ids: Optional list of actor IDs
    :return: QuerySet of filtered movies
    """
    movies = Movie.objects.all()

    if genres_ids and actors_ids:
        # Filter movies that have at least one genre
        # from genres_ids and one actor from actors_ids
        movies = movies.filter(genres__id__in=genres_ids,
                               actors__id__in=actors_ids).distinct()
    elif genres_ids:
        # Filter movies that have at least one genre from genres_ids
        movies = movies.filter(genres__id__in=genres_ids).distinct()
    elif actors_ids:
        # Filter movies that have at least one actor from actors_ids
        movies = movies.filter(actors__id__in=actors_ids).distinct()

    return movies


def get_movie_by_id(movie_id: int) -> Optional[Movie]:
    """
    Retrieve a movie by its ID.

    :param movie_id: ID of the movie
    :return: Movie object or None if not found
    """
    try:
        return Movie.objects.get(id=movie_id)
    except ObjectDoesNotExist:
        return None


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: Optional[List[int]] = None,
                 actors_ids: Optional[List[int]] = None) -> Movie:
    """
    Create a movie with the provided title and
        description, and optionally add genres and actors.

    :param movie_title: Title of the movie
    :param movie_description: Description of the movie
    :param genres_ids: Optional list of genre IDs
    :param actors_ids: Optional list of actor IDs
    :return: Created Movie object
    """
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    if genres_ids:
        genres = Genre.objects.filter(id__in=genres_ids)
        movie.genres.add(*genres)

    if actors_ids:
        actors = Actor.objects.filter(id__in=actors_ids)
        movie.actors.add(*actors)

    return movie
