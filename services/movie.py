from django.db.models import QuerySet
from typing import Optional, List

from db.models import Genre, Movie, Actor


def get_movies(
        genres_ids: Optional[List[int]] = None,
        actors_ids: Optional[List[int]] = None
) -> QuerySet:
    queryset = Movie.objects.all()
    if genres_ids:
        queryset = queryset.filter(genre__id__in=genres_ids)
    if actors_ids:
        queryset = queryset.filter(actor__id__in=actors_ids)

    return queryset

def get_movie_by_id(movie_id: int) -> Optional[Movie]:
    return Movie.objects.get(id=movie_id)

def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: Optional[List[int]] = None,
        actors_ids: Optional[List[int]] = None
) -> Movie:
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    if genres_ids:
        genres = Genre.objects.filter(id__in=genres_ids)
        new_movie.genres.add(*genres)
    if actors_ids:
        actors = Actor.objects.filter(id__in=actors_ids)
        new_movie.actors.add(*actors)

    return new_movie
