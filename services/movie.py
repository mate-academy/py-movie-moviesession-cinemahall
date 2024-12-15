from typing import Optional, List

from db.models import Actor, Genre, Movie


def get_movies(genres_ids: List[int] = None,
               actors_ids: List[int] = None) -> List[dict]:
    # Start with all movies
    movies = Movie.objects.all()

    # Filter by genres if genres_ids are provided
    if genres_ids:
        movies = movies.filter(genres__id__in=genres_ids)

    # Filter by actors if actors_ids are provided
    if actors_ids:
        movies = movies.filter(actors__id__in=actors_ids)

    # Return unique movies (avoid duplicates due to many-to-many relationships)
    return movies.distinct()


def get_movie_by_id(movie_id: int) -> Optional[Movie]:
    """
    Retrieve a movie by its ID.
    """
    try:
        return Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        return None


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: List[int] = None,
                 actors_ids: List[int] = None) -> Movie:
    """
    Create a new movie with the given title, description, genres, and actors.
    """
    # Create the movie
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    # Add genres if provided
    if genres_ids:
        genres = Genre.objects.filter(id__in=genres_ids)
        movie.genres.add(*genres)

    # Add actors if provided
    if actors_ids:
        actors = Actor.objects.filter(id__in=actors_ids)
        movie.actors.add(*actors)

    return movie
