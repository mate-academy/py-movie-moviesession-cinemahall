from typing import List, Optional
from db.models import Movie
from django.db.models import QuerySet


def get_movies(
        genres_ids: Optional[List[int]] = None,
        actors_ids: Optional[List[int]] = None,
) -> QuerySet[Movie]:

    qs = Movie.objects.all()

    if genres_ids:
        qs = qs.filter(genres__id__in=genres_ids)

    if actors_ids:
        qs = qs.filter(actors__id__in=actors_ids)

    return qs.distinct()


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: Optional[List[int]] = None,
        actors_ids: Optional[List[int]] = None,
) -> None:

    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description)
    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)

    return movie
