from db.models import Movie
from django.db.models import QuerySet


def get_movies(genres_ids: list[int] = None, actors_ids: list[int] = None
               ) -> QuerySet:
    """
    Retrieve movies filtered by genres and/or actors.
    """
    queryset = Movie.objects.all()

    if genres_ids and actors_ids:
        queryset = queryset.filter(
            genres__id__in=genres_ids, actors__id__in=actors_ids
        ).distinct()
    elif genres_ids:
        queryset = queryset.filter(genres__id__in=genres_ids).distinct()
    elif actors_ids:
        queryset = queryset.filter(actors__id__in=actors_ids).distinct()

    return queryset


def get_movie_by_id(movie_id: int) -> Movie:
    """
    Retrieve a single movie by its ID.
    """
    try:
        return Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        raise ValueError(f"Movie with id {movie_id} does not exist.")


def create_movie(
    movie_title: str,
    movie_description: str,
    genres_ids: list[int] = None,
    actors_ids: list[int] = None,
) -> Movie:
    movie = Movie.objects.create(
        title=movie_title, description=movie_description
    )
    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)

    return movie
