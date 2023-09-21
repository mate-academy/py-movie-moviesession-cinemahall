from django.db.models import QuerySet
from typing import Optional
from db.models import Movie


def get_movies(genres_ids: Optional[list[int]] = None,
               actors_ids: Optional[list[int]] = None) -> QuerySet:
    queryset = Movie.objects.all()
    if genres_ids:
        queryset = queryset.filter(genres__id__in=genres_ids).distinct()
    if actors_ids:
        queryset = queryset.filter(actors__id__in=actors_ids).distinct()

    return queryset


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 actors_ids: Optional[list[int]] = None,
                 genres_ids: Optional[list[int]] = None) -> None:
    movie = Movie.objects.get_or_create(title=movie_title,
                                        description=movie_description)[0]
    if actors_ids is not None:
        movie.actors.set(actors_ids)
    if genres_ids is not None:
        movie.genres.set(genres_ids)
