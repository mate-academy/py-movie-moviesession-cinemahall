from typing import List, Optional
from django.db.models import QuerySet
from db.models import Movie


def get_movies(
        genres_ids: Optional[List[int]] = None,
        actors_ids: Optional[List[int]] = None) -> QuerySet[Movie]:
    movies = Movie.objects.all()

    if genres_ids and actors_ids:
        movies = movies.filter(
            genres__id__in=genres_ids,
            actors__id__in=actors_ids
        ).distinct()

    elif genres_ids:
        movies = movies.filter(genres__id__in=genres_ids).distinct()

    elif actors_ids:
        movies = movies.filter(actors__id__in=actors_ids).distinct()

    return movies


def get_movie_by_id(movie_id: int) -> Optional[Movie]:

    try:
        movie = Movie.objects.get(id=movie_id)
        return movie
    except Movie.DoesNotExist:
        return None


def create_movie(
    movie_title: str,
    movie_description: str,
    genres_ids: Optional[List[int]] = None,
    actors_ids: Optional[List[int]] = None
) -> Movie:

    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description)

    if genres_ids:
        movie.genres.set(genres_ids)

    if actors_ids:
        movie.actors.set(actors_ids)

    return movie
