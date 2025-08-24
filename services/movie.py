from db.models import Movie, Genre, Actor
from typing import List, Optional
from django.db.models import QuerySet


def get_movies(
    genres_ids: Optional[List[int]] = None,
    actors_ids: Optional[List[int]] = None
) -> QuerySet[Movie]:
    movies_qs = Movie.objects.all()

    if genres_ids:
        movies_qs = movies_qs.filter(genres__id__in=genres_ids).distinct()

    if actors_ids:
        movies_qs = movies_qs.filter(actors__id__in=actors_ids).distinct()

    return movies_qs


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(title: str, description: str,
                 genres_ids: Optional[list[int]] = None,
                 actors_ids: Optional[list[int]] = None) -> Movie:
    movie = Movie.objects.create(title=title, description=description)

    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)

    return movie
