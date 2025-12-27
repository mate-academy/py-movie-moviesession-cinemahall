from db.models import Movie
from django.db import models


def get_movies(genres_ids: list = None,
               actors_ids: list = None) -> models.QuerySet:
    movies = Movie.objects.all()
    if not genres_ids and not actors_ids:
        return movies
    elif not genres_ids and actors_ids:
        return movies.filter(actors__id__in=actors_ids).distinct()
    elif not actors_ids and genres_ids:
        return movies.filter(genres__id__in=genres_ids).distinct()
    else:
        return movies.filter(genres__id__in=genres_ids,
                             actors__id__in=actors_ids).distinct()


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: list = None,
                 actors_ids: list = None) -> Movie | None:
    movies_set = Movie.objects.create(title=movie_title,
                                      description=movie_description)
    if actors_ids:
        movies_set.actors.set(actors_ids)
    if genres_ids:
        movies_set.genres.set(genres_ids)
    return movies_set
