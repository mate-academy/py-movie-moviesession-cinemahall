from typing import List, Optional

from django.db.models import QuerySet

from db.models import Movie


def get_movies(
        genres_ids: Optional[List[int]] = None,
        actors_ids: Optional[List[int]] = None
) -> QuerySet[Movie]:

    queryset = Movie.objects.all()
    if genres_ids is None and actors_ids is None:
        return queryset

    if genres_ids is not None:
        queryset = queryset.filter(genres__id__in=genres_ids)

    if actors_ids is not None:
        queryset = queryset.filter(actors__id__in=actors_ids)
    return queryset


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: Optional[List[int]] = None,
        actors_ids: Optional[List[int]] = None
) -> Movie:
    created_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if actors_ids:
        created_movie.actors.set(actors_ids)

    if genres_ids:
        created_movie.genres.set(genres_ids)

    return created_movie
