from db.models import Movie, Genre, Actor
from typing import Optional, List
from django.db.models import QuerySet  # Add this import


def get_movies(
    genres_ids: Optional[List[int]] = None,
    actors_ids: Optional[List[int]] = None,
) -> QuerySet[Movie]:
    """Retrieve movies filtered by genres and/or actors."""
    queryset = Movie.objects.all()
    if genres_ids:
        queryset = queryset.filter(genres__id__in=genres_ids).distinct()
    if actors_ids:
        queryset = queryset.filter(actors__id__in=actors_ids).distinct()
    return queryset


def get_movie_by_id(movie_id: int) -> Optional[Movie]:
    """Retrieve a movie by its ID."""
    return Movie.objects.filter(id=movie_id).first()


def create_movie(
    movie_title: str,
    movie_description: str,
    genres_ids: Optional[List[int]] = None,
    actors_ids: Optional[List[int]] = None,
) -> Movie:
    """Create a movie with optional genres and actors."""
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    if genres_ids:
        genres = Genre.objects.filter(id__in=genres_ids)
        movie.genres.set(genres)
    if actors_ids:
        actors = Actor.objects.filter(id__in=actors_ids)
        movie.actors.set(actors)
    return movie
