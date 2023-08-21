from db.models import Movie, Actor, Genre
from django.db.models import QuerySet
from typing import Optional


def get_movies(
        genres_ids: Optional[list[int]] = None,
        actors_ids: Optional[list[int]] = None
) -> QuerySet[Movie]:
    if not genres_ids and not actors_ids:
        movies = Movie.objects.all()
    elif genres_ids and actors_ids:
        movies = Movie.objects.filter(
            genres__id__in=genres_ids,
            actors__id__in=actors_ids
        ).distinct()
    elif genres_ids:
        movies = Movie.objects.filter(genres__id__in=genres_ids).distinct()
    elif actors_ids:
        movies = Movie.objects.filter(actors__id__in=actors_ids).distinct()
    return movies


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: Optional[list[int]] = None,
        actors_ids: Optional[list[int]] = None) -> QuerySet[Movie]:

    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description)

    if genres_ids:
        genres = Genre.objects.filter(id__in=genres_ids)
        movie.genres.set(genres)
    if actors_ids:
        actors = Actor.objects.filter(id__in=actors_ids)
        movie.actors.set(actors)
    return movie
