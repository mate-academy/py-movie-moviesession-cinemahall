from typing import List, Optional
from db.models import Movie, Actor, Genre
from django.db.models.query import QuerySet


def get_movies(
    genres_ids: Optional[List[int]] = None,
    actors_ids: Optional[List[int]] = None
) -> QuerySet[Movie]:
    queryset = Movie.objects.all()

    if genres_ids:
        # Poprawny filtr po ID relacji ManyToMany
        queryset = queryset.filter(genres__id__in=genres_ids).distinct()

    if actors_ids:
        # Poprawny filtr po ID relacji ManyToMany
        queryset = queryset.filter(actors__id__in=actors_ids).distinct()

    return queryset


def get_movie_by_id(movie_id: int) -> Movie:
    # Zwraca instancję modelu; wyjątek DoesNotExist propaguje się
    return Movie.objects.get(id=movie_id)


def create_movie(
    movie_title: str,
    movie_description: str,
    genres_ids: Optional[List[int]] = None,
    actors_ids: Optional[List[int]] = None
) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )

    if genres_ids:
        movie.genres.set(Genre.objects.filter(id__in=genres_ids))

    if actors_ids:
        movie.actors.set(Actor.objects.filter(id__in=actors_ids))

    return movie
