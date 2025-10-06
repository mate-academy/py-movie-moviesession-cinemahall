from typing import Iterable, Optional
from django.db.models import QuerySet

from db.models import Movie


def get_movies(genres_ids: Optional[Iterable[int]] = None,
               actors_ids: Optional[Iterable[int]] = None) -> QuerySet[Movie]:
    """
    If genres_ids and actors_ids are not provided,
    the method returns all movies
    If both genres_ids and actors_ids are provided,
    the method returns movies,
    that have at least one genre from genres_ids and
    one actor from actors_ids.
    If only genres_ids is provided, the method returns
    the queryset with movies,
    that have at least one genre from genres_ids
    If only actors_ids is provided, the method returns
    the queryset with movies,
    that have at least one actor from actors_ids
    """
    queryset = Movie.objects.all()
    if genres_ids:
        queryset = queryset.filter(genres__id__in=genres_ids)

    if actors_ids:
        queryset = queryset.filter(actors__id__in=actors_ids)

    return queryset.distinct()


def get_movie_by_id(movie_id: int) -> Movie:
    """
    Returns movie by id
    """
    return Movie.objects.get(id=movie_id)


def create_movie(*, movie_title: str,
                 movie_description: str,
                 genres_ids: Optional[Iterable[int]] = None,
                 actors_ids: Optional[Iterable[int]] = None) -> Movie:
    """
    create_movie, takes movie_title, movie_description,
    optional genres_ids and
    optional actors_ids, genres_ids and actors_ids are the
    list of genres ids and
    the list of actors ids respectively, method creates
    movie with provided title and description
    """
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )

    if genres_ids:
        movie.genres.set(genres_ids)

    if actors_ids:
        movie.actors.set(actors_ids)

    return movie
