from typing import List, Optional
from django.db.models import Q, QuerySet
from db.models import Movie


def get_movies(
        genres_ids: Optional[List[int]] = None,
        actors_ids: Optional[List[int]] = None) -> QuerySet[Movie]:
    query = Q()
    if genres_ids:
        query &= Q(genres__id__in=genres_ids)
    if actors_ids:
        query &= Q(actors__id__in=actors_ids)
    return Movie.objects.filter(query).distinct()


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
    movie_title: str,
    movie_description: str,
    genres_ids: Optional[List[int]] = None,
    actors_ids: Optional[List[int]] = None
) -> Movie:
    movie = Movie(title=movie_title, description=movie_description)
    movie.save()
    if genres_ids:
        movie.genres.add(*genres_ids)
    if actors_ids:
        movie.actors.add(*actors_ids)

    movie.save()
    return movie
